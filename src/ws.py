import asyncio
import websockets

async def websocket_handler(websocket):
    while True:
        message = await websocket.recv()
        # Retrieving message from request
        print(f"Received message: {message}")

        response = f"You say: {message}"
        # Responding to user
        await websocket.send(response)

async def main():
    start_server = await websockets.serve(websocket_handler, 'localhost', 8765)
    await start_server.wait_closed()

# Run the event loop with asyncio.run()
asyncio.run(main())
