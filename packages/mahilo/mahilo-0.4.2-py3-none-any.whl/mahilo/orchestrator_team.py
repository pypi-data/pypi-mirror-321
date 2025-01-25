from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uuid
import asyncio
from typing import Dict, List, Union
import websockets
from pydantic import BaseModel
import subprocess
import os
import signal

class ServerConfig(BaseModel):
    openai_api_key: str

class Orchestrator:
    def __init__(self):
        self.app = FastAPI()
        self.active_servers: Dict[str, dict] = {}  # server_id -> {process, port, agent_types}
        self.websocket_connections: Dict[str, Dict[str, WebSocket]] = {}
        self.base_port = 8001  # Reserve 8000 for the orchestrator
        
        # Setup CORS
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        
        # Define fixed agent types - these match the names in control_plane.py
        self.agent_types = ["ProductAgent", "MarketingAgent", "SalesAgent"]
        
        self._setup_routes()

    def _setup_routes(self):
        @self.app.post("/create-server")
        async def create_server(config: ServerConfig):
            server_id = str(uuid.uuid4())
            port = self._get_available_port()
            
            if config.openai_api_key == "":
                config.openai_api_key = os.getenv("OPENAI_API_KEY")
            
            try:
                process = await self._start_game_server(
                    port,
                    config.openai_api_key,
                    server_id
                )
                
                self.active_servers[server_id] = {
                    "process": process,
                    "port": port,
                    "agent_types": self.agent_types
                }
                
                return {"server_id": server_id, "port": port}
            
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

        @self.app.websocket("/ws/{server_id}/{agent_type}")
        async def websocket_proxy(websocket: WebSocket, server_id: str, agent_type: str):
            # Add debug logging
            print(f"WebSocket connection attempt for server {server_id}, agent {agent_type}")

            if server_id not in self.active_servers:
                await websocket.close(code=1008, reason="Server not found")
                return
                
            server_info = self.active_servers[server_id]
            if agent_type not in server_info["agent_types"]:
                await websocket.close(code=1008, reason="Invalid agent type")
                return
                
            await websocket.accept()
            connection_id = str(uuid.uuid4())
            
            if server_id not in self.websocket_connections:
                self.websocket_connections[server_id] = {}
            self.websocket_connections[server_id][connection_id] = websocket
            
            try:
                # Connect to the game server process
                server_ws_url = f"ws://localhost:{server_info['port']}/ws/{agent_type}"
                async with websockets.connect(server_ws_url) as server_ws:
                    await asyncio.gather(
                        self._forward_messages(websocket, server_ws),
                        self._forward_messages(server_ws, websocket)
                    )
            except WebSocketDisconnect:
                if server_id in self.websocket_connections:
                    self.websocket_connections[server_id].pop(connection_id, None)
                    # If no more connections, cleanup the server
                    if not self.websocket_connections[server_id]:
                        await self._cleanup_server(server_id)
            except Exception as e:
                print(f"Error in websocket proxy: {str(e)}")

        @self.app.websocket("/health")
        async def health_check(websocket: WebSocket):
            await websocket.accept()
            await websocket.close()

        @self.app.on_event("shutdown")
        async def shutdown_event():
            # Cleanup all running servers
            for server_id in list(self.active_servers.keys()):
                await self._cleanup_server(server_id)

    async def _start_game_server(self, port: int, openai_key: str, server_id: str) -> subprocess.Popen:
        env = os.environ.copy()
        env.update({
            "OPENAI_API_KEY": openai_key,
            "PORT": str(port),
            "SERVER_ID": server_id
        })
        
        cmd = ["python", "examples/team_of_agents/control_plane.py"]
        
        process = subprocess.Popen(
            cmd,
            env=env,
            preexec_fn=os.setsid
        )
        
        # Wait for the server to start
        await self._wait_for_server(port)
        return process

    async def _wait_for_server(self, port: int, timeout: int = 30):
        start_time = asyncio.get_event_loop().time()
        while (asyncio.get_event_loop().time() - start_time) < timeout:
            try:
                async with websockets.connect(f"ws://localhost:{port}/health") as ws:
                    await ws.close()
                    return
            except:
                await asyncio.sleep(0.1)
        raise Exception(f"Server failed to start on port {port}")

    async def _cleanup_server(self, server_id: str):
        if server_id in self.active_servers:
            server_info = self.active_servers[server_id]
            # Kill the process group
            try:
                os.killpg(os.getpgid(server_info["process"].pid), signal.SIGTERM)
            except:
                pass
            del self.active_servers[server_id]
            if server_id in self.websocket_connections:
                del self.websocket_connections[server_id]

    def _get_available_port(self) -> int:
        used_ports = {server["port"] for server in self.active_servers.values()}
        port = self.base_port
        while port in used_ports:
            port += 1
        return port

    async def _forward_messages(self, source: Union[WebSocket, websockets.WebSocketClientProtocol], 
                              destination: Union[WebSocket, websockets.WebSocketClientProtocol]):
        try:
            while True:
                # Handle receiving based on source type
                if isinstance(source, WebSocket):
                    message = await source.receive_text()
                else:  # WebSocketClientProtocol
                    message = await source.recv()
                    
                # Handle sending based on destination type
                if isinstance(destination, WebSocket):
                    await destination.send_text(message)
                else:  # WebSocketClientProtocol
                    await destination.send(message)
                    
        except (WebSocketDisconnect, websockets.exceptions.ConnectionClosed):
            pass

    def run(self, host: str = "0.0.0.0", port: int = 8000):
        import uvicorn
        uvicorn.run(self.app, host=host, port=port)

if __name__ == "__main__":
    orchestrator = Orchestrator()
    orchestrator.run() 