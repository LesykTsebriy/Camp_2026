import uvicorn
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from typing import List

app = FastAPI()

# Keeps track of EVERYONE connected (browsers and machine scripts alike)
connected_clients: List[WebSocket] = []

html_content = """
<!DOCTYPE html>
<html>
    <head><title>Live WebSocket Stream</title></head>
    <body style="font-family: Arial, sans-serif; margin: 40px; background: #f4f6f9;">
        <h1>Display Server (Port 8000)</h1>
        <p>Status: <span id="status" style="color: red; font-weight: bold;">Disconnected</span></p>
        
        <h3>Live Machine Data Feed:</h3>
        <ul id="stream" style="background: white; padding: 20px; border-radius: 5px; min-height: 150px; border: 1px solid #ccc;"></ul>

        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onopen = () => {
                document.getElementById("status").innerText = "Connected & Listening for Machine...";
                document.getElementById("status").style.color = "green";
            };
            ws.onmessage = (event) => {
                var stream = document.getElementById('stream');
                var item = document.createElement('li');
                item.innerText = event.data;
                stream.appendChild(item);
            };
            ws.onclose = () => {
                document.getElementById("status").innerText = "Disconnected";
                document.getElementById("status").style.color = "red";
            };
        </script>
    </body>
</html>
"""

@app.get("/")
async def get_ui():
    return HTMLResponse(html_content)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.append(websocket)
    try:
        while True:
            # Wait for data to fly in from the Machine Script
            data = await websocket.receive_text()
            
            # Broadcast whatever the machine sends to EVERYONE (including your browser)
            for client in connected_clients:
                await client.send_text(f"[Machine Feed]: {data}")
    except WebSocketDisconnect:
        connected_clients.remove(websocket)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
