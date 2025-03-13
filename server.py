import os
import asyncio
import websockets

PORT = int(os.getenv("PORT", 8765))  # Render के दिए गए पोर्ट को एक्सेप्ट करें
HOST = "0.0.0.0"

connected_clients = set()

async def handler(websocket, path):
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            for client in connected_clients:
                if client != websocket:
                    await client.send(message)
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        connected_clients.remove(websocket)

async def main():
    server = await websockets.serve(handler, HOST, PORT)
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())
