from py2neo import Graph, Node, Relationship
import json

graph = Graph(
    "http://localhost:7474",
    username="neo4j",
    password="123456"
)

with open("../data/data.json", 'r', encoding='utf-8') as load_f:
    data = json.load(load_f)


# root, leaf, stem, flower, fruit 作为子节点
for elem in data['data']:
    # animal主节点
    node = Node(
        "plant",
        name=elem['name'],
        belong=elem['belong'],
        name_cn=elem['name_cn'],
        name_en=elem['name_en'],
        shape=elem['shape'],
        position=elem['position'],
        environment=elem['environment'],
        document=elem['document'],
        behavior=elem['behavior']
    )
    #  root子节点
    root = Node(
        "root",
        old=elem['root']['old'],
        length=elem['root']['length'],
        color=elem['root']['color']
    )
    # leaf子节点
    leaf = Node(
        "leaf",
        old=elem['leaf']['old'],
        length=elem['leaf']['length'],
        color=elem['leaf']['color']
    )
    # stem子节点
    stem = Node(
        "stem",
        old=elem['stem']['old'],
        length=elem['stem']['length'],
        color=elem['stem']['color']
    )
    # flower子节点
    flower = Node(
        "flower",
        old=elem['flower']['old'],
        time=elem['flower']['time'],
        color=elem['flower']['color']
    )
    # fruit子节点
    fruit = Node(
        "fruit",
        old=elem['fruit']['old'],
        length=elem['fruit']['length'],
        color=elem['fruit']['color']
    )

    # 建立关系
    node_root = Relationship(node, "has", root)
    node_flower = Relationship(node, "has", flower)
    node_stem = Relationship(node, "has", stem)
    node_leaf = Relationship(node, "has", leaf)
    node_fruit = Relationship(node, "has", fruit)

    subgraph = node_root | node_flower | node_stem | node_leaf | node_fruit

    graph.create(subgraph)




