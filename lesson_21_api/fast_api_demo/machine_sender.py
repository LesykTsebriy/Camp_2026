import asyncio
import websockets

async def connect_to_server():
    uri = "ws://localhost:8000/ws"
    
    print(f"Connecting to Display Server at {uri}...")
    
    # This establishes a permanent, constant WebSocket connection from your machine to the server
    async with websockets.connect(uri) as websocket:
        print("Successfully connected! The pipe is wide open.")
        print("Type anything below and press Enter to stream it:")
        print("-" * 50)
        
        while True:
            # Run in an executor so typing doesn't block the async loop
            user_input = await asyncio.to_thread(input, "Send Data -> ")
            
            if user_input.strip():
                # Shoot the data straight through the permanent WebSocket pipe
                await websocket.send(user_input)

if __name__ == "__main__":
    try:
        asyncio.run(connect_to_server())
    except KeyboardInterrupt:
        print("\nDisconnected from server.")
    except ConnectionRefusedError:
        print("\nError: Could not connect. Is display_server.py running on port 8000?")
