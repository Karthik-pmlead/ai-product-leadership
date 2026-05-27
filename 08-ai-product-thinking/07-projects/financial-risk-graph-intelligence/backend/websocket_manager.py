clients = []


async def broadcast(data):

    dead = []

    for c in clients:
        try:
            await c.send_json(data)
        except:
            dead.append(c)

    for d in dead:
        clients.remove(d)
