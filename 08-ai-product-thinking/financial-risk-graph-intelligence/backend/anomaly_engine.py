from graph_engine import graph


def detect_anomalies():

    anomalies = []

    for n in graph.nodes:

        degree = len(list(graph.neighbors(n)))
        risk = graph.nodes[n]["risk"]

        if degree >= 2 and risk >= 40:

            anomalies.append({
                "entity": graph.nodes[n]["label"],
                "risk": risk,
                "connections": degree,
                "reason": "Highly connected high-risk entity"
            })

    return anomalies
