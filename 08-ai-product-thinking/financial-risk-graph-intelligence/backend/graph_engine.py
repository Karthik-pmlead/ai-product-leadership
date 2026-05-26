import networkx as nx
from data.graph_seed import nodes, edges

graph = nx.Graph()

for n in nodes:
    graph.add_node(
        n["id"],
        label=n["label"],
        type=n["type"],
        risk=n["risk"]
    )

for e in edges:
    graph.add_edge(*e)


def get_graph_data():
    return {
        "nodes": [
            {
                "id": n,
                **graph.nodes[n]
            }
            for n in graph.nodes
        ],
        "edges": [
            {
                "source": e[0],
                "target": e[1]
            }
            for e in graph.edges
        ]
    }
