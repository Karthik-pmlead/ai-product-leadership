clients = []

async def broadcast(data):

    disconnected = []

    for client in clients:

        try:
            await client.send_json(data)

        except:
            disconnected.append(client)

    # cleanup dead clients
    for d in disconnected:

        clients.remove(d)

