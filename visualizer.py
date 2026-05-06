from pyvis.network import Network
import numpy as np

def saveGraph(graph, output, report ):
    nt = Network(height='750px', width='100%', bgcolor="#222222",font_color="white", directed=True)
    
    for node in graph.nodes:
        graph.nodes[node]['color'] = "#3498db"

        if node in report['orphans']:
            graph.nodes[node]['color'] = "#95a5a6"
            graph.nodes[node]['title'] = "⚠️ Fichier orphelin (non utilisé)"

        # Si le nœud fait partie d'un cycle -> on le met en rouge
        for cycle in report['cycles']:
            if node in cycle:
                graph.nodes[node]['color'] = "#e74c3c"
                graph.nodes[node]['title'] = "❌ Dépendance circulaire détectée !"

    nt.from_nx(graph)
    nt.toggle_physics(True)
    try:
        nt.write_html(output)
        print(f"Success! Open '{output}' in your browser to see the graph.")
    except Exception as e:
        print(f"Error saving graph: {e}")
