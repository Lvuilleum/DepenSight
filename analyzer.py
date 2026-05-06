import pyvis.network
import networkx as nx

def check_health(G):
    report = {
        "cycles": list(nx.simple_cycles(G)),
        "orphans": [n for n, deg in G.in_degree() if deg == 0 and n != "main"],
        "bottlenecks": sorted(nx.betweenness_centrality(G).items(), key=lambda x: x[1], reverse=True)[:3]
    }
    return report