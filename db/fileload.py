from py2neo import Graph, Node
import re
graph = Graph(
    "http://localhost:7474",
    username="neo4j",
    password="123456"
)

file = open("../data/data_source.txt", "r", encoding="UTF-8")

# line = re.split("\s\s+", file.readline())
# for i in line:
#     print(i)
for line in file.readlines():
    line = re.split("\s\s+", line)
    if len(line) < 6:

        continue
    node = Node("plant", name1=line[0], name=line[1], category=line[2], info1=line[3], info2=line[4], info3=line[-1])
    graph.create(node)
    print("Create Node: " + line[1] + "\t" + line[2])

file.close()