import requests
import json
from bs4 import BeautifulSoup
import py2neo
import re

#参数设置
TIME_OUT = 3
HEADERS = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'Cookie': 'JSESSIONID=BB1780036683835AED712D3AE3F0A6B8',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'www.sp2000.org.cn',
    'Referer': 'http://www.sp2000.org.cn/browse/browse_taxa',
    'X-CSRF-TOKEN': 'c6303cb8-e9ee-4dc6-be25-114f3df99027',
}

LABEL_ANIMAL = 'animal'
LABEL_PLANT = 'plant'
NODE_ANIMAL_CODE = "994ce8b6-25c8-4ca7-999b-a40bf40c9ff3"
NODE_PLANT_CODE = "b9eff58a-2133-44d0-8bd5-2cc019dd1a31"

#爬取网站

test_url = "http://www.sp2000.org.cn/browse/taxa_tree_children"
#请求
# res = requests.post(test_url, headers=HEADERS)
# html = res.json()
# print(html)

#数据库
graph = py2neo.Graph(
    "http://localhost:7474",
    username="neo4j",
    password="123456"
)

#匹配中文
def match_ch(text):
    regex_str = ".*?([\u4E00-\u9FA5]+).*?"
    match_obj = re.findall(regex_str, text)
    if match_obj:
        return match_obj[0]
    else:
        return text

def init_node():
    data = requests.post(test_url, headers=HEADERS).json()
    node_animal = py2neo.Node("animal", code=data[0]['id'], name=match_ch(data[0]['name']))
    node_plant = py2neo.Node("plant", code=data[4]['id'], name=match_ch(data[4]['name']))

    graph.create(node_animal)
    graph.create(node_plant)

    print("Init Graph Nodes.")

    return [node_animal, node_plant]

def get_data_by_id(id):
    data = requests.post(test_url, headers=HEADERS, data={'id':id}).json()
    rst = []
    for i in data:
        rst.append({
            'id': i['id'],
            'name': match_ch(i['name'])
        })
    return rst

def create_node(label, code, name, parent_code=None):
    node1 = graph.nodes.match(label, code=code).first()
    if node1:
        print("Node: " + name + " exists!")
        pass
    else:
        node = py2neo.Node(label, code=code, name=name)
        graph.create(node)
        print("Create Node: " + name)

        if parent_code:
            parent_node = graph.nodes.match(label, code=parent_code).first()
            #print(parent_node)
            rel = py2neo.Relationship(node, "属于", parent_node)
            graph.create(rel)
            print("Create Relationship between Node " + name + " and Node " + parent_node['name'])

def expand_node_by_id(label, id):
    nodes_list = get_data_by_id(id)
    p_node = graph.nodes.match(label, code=id).first()

    rst = []

    for node in nodes_list:
        #TODO
        create_node(label, node['id'], node['name'], p_node['code'])
        rst.append({
            'id': node['id'],
            'name': node['name']
        })

    return rst

def array_flat(lists):
    rst = []
    for list in lists:
        for i in list:
            rst.append(i)

    return rst

def expand_node_by_list(label, list):
    rst = []
    for node_data in list:
        tmp = expand_node_by_id(label, node_data['id'])
        rst.append(tmp)

    return array_flat(rst)




def main():
    #init_node()
    #animal_list = get_data_by_id('994ce8b6-25c8-4ca7-999b-a40bf40c9ff3')
    #动物界相关
    #门
    nodes_animal_men = expand_node_by_id(LABEL_ANIMAL, NODE_ANIMAL_CODE)
    nodes_animal_gang = expand_node_by_list(LABEL_ANIMAL, nodes_animal_men)
    nodes_animal_mu = expand_node_by_list(LABEL_ANIMAL, nodes_animal_gang)
    nodes_animal_ke = expand_node_by_list(LABEL_ANIMAL, nodes_animal_mu)
    nodes_animal_shu = expand_node_by_list(LABEL_ANIMAL, nodes_animal_ke)
    nodes_entity = expand_node_by_list(LABEL_ANIMAL, nodes_animal_shu)
    print(nodes_entity)

main()
