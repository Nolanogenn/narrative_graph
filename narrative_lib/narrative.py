from rdflib import Graph
import narrative_domain

default_graph = '../data/narration_ontology.ttl'
shapes = '../data/shapes.ttl'

def new_graph(t,name):
    g = Graph()
    g.parse(default_graph)
    n = narrative_domain.create_graph(t,name) 
    g.add(n)
    return g

def save_graph(graph, path):
    graph.serialize(destination=path)
    return True

def load_graph(path):
    g = Graph()
    return g.parse(path)

def add_edge(graph, edge):
    g.add(edge)
    return 1

def remove_edge(graph, edge):
    g.remove(edge)
    return 1

if __name__ == "__main__":
    g = new_graph('environmental', 'TestEnvironmental')
    narrative_domain.add_environmental_node(
            g,
            name = "valonde",
            kind = "Place"
            )
    save_graph(g, 'test.ttl')


