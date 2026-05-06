# scanner to scan the directorey and give dependencies -> graph manager -> vizualiser -> analyzer to analyze the risk 
import scanner
import graph_manager
import visualizer

def run_visualizer(target_directory):
    files = scanner.findFile(target_directory)

    G = graph_manager.initialize()

    for file_path in files:
        deps = scanner.findDependence(file_path)

        graph_manager.addModuleNode(G, file_path.name, is_local=True)

        for d in deps:
            graph_manager.addModuleNode(G, d, is_local=False)
            graph_manager.addDependence(G, file_path.name, d)
    
    visualizer.saveGraph(G, "dependencies.html")

if __name__ == "__main__":
    run_visualizer(".")