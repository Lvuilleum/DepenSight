from pyvis.network import Network


def saveGraph(graph, output):
    nt = Network(height='750px', width='100%', bgcolor="#222222",font_color="white", directed=True)
    nt.from_nx(graph)
    nt.toggle_physics(True)
    try:
        nt.write_html(output)
        print(f"Success! Open '{output}' in your browser to see the graph.")
    except Exception as e:
        print(f"Error saving graph: {e}")
