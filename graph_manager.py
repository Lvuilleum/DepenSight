import networkx as nx
import os 
import numpy as np

def addModuleNode(graph, name, is_local=True):
    if name not in graph:
        color = "#3498db" if is_local else "#95a5a6"
        graph.add_node(name, label=name, color=color, title=f"Type: {'Local' if is_local else 'External'}")


def initialize():
    return nx.DiGraph()


def addDependence(graph, source, target):
    graph.add_edge(source, target)