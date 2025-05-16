from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import SKOS, RDF

nr = Namespace('https://www.genn.nolalt.org/ontologies/narration#')

def get_graph_node(g):
    node_query = """
        PREFIX nr: <https://www.genn.nolalt.org/ontologies/narration#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

        SELECT DISTINCT ?node ?any
        WHERE {
        ?node a ?graph .
        ?graph skos:broader ?any .
        }
        LIMIT 1
    """
    qres = g.query(node_query)
    return qres

def create_graph(t,name):
    if t not in ['environmental', 'event']:
        raise Exception('graph type should be one of ["environmental", "event"]')
    if t == 'environmental':
        toret = (nr[name], RDF.type, nr['EnvironmentalGraph'])
    else:
        toret = (nr[name], RDF.type, nr['EventGraph'])
    return toret

def add_environmental_node(g, **kwargs):
    nodeName = kwargs["name"]
    environmental_type = kwargs["kind"]
    rootNode = list(get_graph_node(g))[0].node
    g.add((nr[nodeName], RDF.type, nr[environmental_type]))
    g.add((rootNode, nr['contains'], nr[nodeName]))

