from py2neo import Graph, Node, Relationship

test_graph = Graph(
    "http://localhost:7474",
    username="neo4j",
    password="123456"
)

node1 = test_graph.nodes.match("animal", code="b122f437-de89-4503-8bbc-e4f4eec2762a").first()
test_graph.delete(node1)

