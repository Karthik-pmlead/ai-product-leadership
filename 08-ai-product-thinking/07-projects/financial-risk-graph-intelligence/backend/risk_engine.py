from graph_engine import graph


def propagate_risk(entity_id, delta):

    if entity_id not in graph:
        return

    # update selected node
    graph.nodes[entity_id]["risk"] += delta

    # propagate to neighbors
    for neighbor in graph.neighbors(entity_id):

        current = graph.nodes[neighbor]["risk"]

        propagated = int(delta * 0.4)

        graph.nodes[neighbor]["risk"] = min(
            current + propagated,
            100
        )


def get_high_risk_nodes():

    risky = []

    for n in graph.nodes:

        risk = graph.nodes[n]["risk"]

        if risk >= 50:
            risky.append({
                "id": n,
                "label": graph.nodes[n]["label"],
                "risk": risk
            })

    return risky
