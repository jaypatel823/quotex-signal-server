async def echo(websocket, path):
    try:
        print("✅ Client Connected!")
        async for message in websocket:
            print(f"📩 Message Received: {message}")
            await websocket.send(f"🔄 Echo: {message}")
    except websockets.exceptions.ConnectionClosed as e:
        print(f"❌ Connection Closed: {e}")
