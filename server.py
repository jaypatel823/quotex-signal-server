import asyncio
import websockets
import os

PORT = int(os.getenv("PORT", 10000))  # Render का पोर्ट सेट करें
HOST = "0.0.0.0"

async def echo(websocket, path):
    print("✅ Client Connected!")
    try:
        async for message in websocket:
            print(f"📩 Message Received: {message}")
            await websocket.send(f"🔄 Echo: {message}")  # रिस्पांस भेजना
    except websockets.exceptions.ConnectionClosed as e:
        print(f"❌ Connection Closed: {e}")

async def main():
    print(f"🚀 WebSocket Server Starting on ws://{HOST}:{PORT} ...")
    try:
        server = await websockets.serve(echo, HOST, PORT)
        await server.wait_closed()
    except Exception as e:
        print(f"❌ Server Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
