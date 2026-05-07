from pyvis.network import Network
import networkx as nx

def saveGraph(graph, output_filename, report):
    """
    Transforme le graphe NetworkX en interface interactive 
    en utilisant les données de l'analyzer.
    """
    net = Network(
        height="750px", 
        width="100%", 
        bgcolor="#1a1a1a", 
        font_color="white", 
        directed=True, 
        notebook=False
    )

    bottleneck_names = [item[0] for item in report.get('bottlenecks', [])]

    for node in graph.nodes:
        node_data = report.get('nodes', {}).get(node, {})
        risk = node_data.get('risk_score', 0)
        impact = node_data.get('impact', 0)
        
        risk_val = float(risk) if risk else 0
        graph.nodes[node]['size'] = 15 + (risk_val * 0.5) 
        
        if node_data.get('is_in_cycle'):
            graph.nodes[node]['color'] = "#e74c3c"  # Rouge (Danger)
        elif node in bottleneck_names:
            graph.nodes[node]['color'] = "#f1c40f"
        elif node_data.get('is_orphan'):
            graph.nodes[node]['color'] = "#95a5a6"  # Gris (Orphelin)
        else:
            graph.nodes[node]['color'] = "#3498db"  # Bleu (Local)
            
        graph.nodes[node]['label'] = node

        tooltip_content = (f"Module: {node}, "
                           f"Risk Score: {risk_val:.2f}, "
                           f"Impact Radius: {impact} files")
        
        if node in bottleneck_names:
             tooltip_content += ", Architectural Bridge (Bottleneck)"

        graph.nodes[node]['title'] = f"{tooltip_content}"

    net.from_nx(graph)
    
    net.toggle_physics(True)
    
    net.write_html(output_filename)
    print(f"Success! Graph generated: {output_filename}")