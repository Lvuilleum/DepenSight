import pyvis.network
import networkx as nx

def check_health(G):
    page_rank = get_pagerank(G)
    try:
        all_cycles = list(nx.simple_cycles(G))
    except:
        all_cycles = []
    
    node_details = {}
    for node in G.nodes:
        node_details[node] = {
            "risk_score": calculate_node_risk(node, G, page_rank),
            "is_orphan": G.in_degree(node) == 0 and node != "main",
            "is_in_cycle": any(node in cycle for cycle in all_cycles),
            "impact": get_impact_radius(G, node),
        }

    report = {
        "nodes": node_details,
        "cycles": list(nx.simple_cycles(G)),
        "orphans": [n for n, deg in G.in_degree() if deg == 0 and n != "main"],
        "bottlenecks": sorted(nx.betweenness_centrality(G).items(), key=lambda x: x[1], reverse=True)[:3]
    }

    
    return report



#Renvoie le dictionnaire des scores d'importance
def get_pagerank(G): 
    return nx.pagerank(G) 


# Calcule le nombre de descendants pour un fichier précis
def get_impact_radius(G, node): 
    return len(nx.descendants(G, node)) 


def calculate_node_risk(node, G, pagerank_scores):
    importance = pagerank_scores.get(node, 0)
    impact = get_impact_radius(G, node)
    
    risk_score = (importance * 100 *  0.7) + (impact * 0.3)
    return round(risk_score,2)

