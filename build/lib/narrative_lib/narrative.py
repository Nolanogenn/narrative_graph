from rdflib import Graph

default_graph = '../data/narration_ontology.ttl'
shapes = '../data/shapes.ttl'

def new_graph():
    g = Graph()
    return g.parse(default_graph)

def save_graph(graph, path):
    graph.serialize(destination=path)
    return True

def load_graph(path):
    g = Graph()
    return g.parse(path)


