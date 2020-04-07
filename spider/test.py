import requests
import json
from bs4 import BeautifulSoup

#参数设置
TIME_OUT = 3
HEADERS = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'Cookie': 'JSESSIONID=2EC0673EC3930162D446EFE7E39694F5',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'www.sp2000.org.cn',
    'Referer': 'http://www.sp2000.org.cn/browse/browse_taxa',
    'X-CSRF-TOKEN': 'f3b98b97-c101-4b0c-9ee3-8e33f86c38f1',
}


#爬取网站
MAIN_URL = "http://pcdb.wbgcas.cn/page/showEntity.vpage?uri=cn.csdb.whbgip.plantpic#"
BASE_URL = "http://pcdb.wbgcas.cn/"

#test_url = "http://pcdb.wbgcas.cn/!doQuery.vpage"
test_url = "http://www.sp2000.org.cn/browse/taxa_tree_children"
#请求
res = requests.post(test_url, headers=HEADERS)
html = res.text

#结果处理 bs4
# soup = BeautifulSoup(html, "html.parser")
# data = json.loads(soup.text)
#
# post_data = {
#     'id':data[0]['id'],
# }
# res2 = requests.post(test_url, headers=HEADERS, data=post_data)
# print(res2.text)

url_dict = {
    'lv0': [test_url]
}


def get_ids_root(url, post_data={}):
    list = []

    res = requests.post(test_url, headers=HEADERS, data=post_data)
    data = res.json()

    for i in data:
        list.append(i['id'])
    return list

def get_ids_jie(id_list):
    rst_list = []
    post_data = {}

    for id in id_list:
        post_data['id'] = id
        raw_data = requests.post(test_url, headers=HEADERS, data=post_data).json()
        for i in raw_data:
            # rst_list.append({
            #     'id': i['id'],
            #     'name': i['name']
            # })
            rst_list.append(i['id'])

    return rst_list


ids_root = get_ids_root(test_url)
id_animal = ids_root[0]
id_plant = ids_root[4]

# p_data = {}
# # p_data['id'] = id_animal
# # ids_animal_men = get_ids_root(test_url, post_data=p_data)
# # ids_animal_gang = get_ids_jie(ids_animal_men)
# # ids_animal_mu = get_ids_jie(ids_animal_gang)
# # ids_animal_ke = get_ids_jie(ids_animal_mu)
# # ids_animal_shu = get_ids_jie(ids_animal_ke)
# # ids_animal = get_ids_jie(ids_animal_shu)
# # print(ids_animal_shu)

t = requests.get("http://www.sp2000.org.cn/species/show_species_details/754d0149-7858-4b46-8cef-bf30cabf0b3a").text
soup = BeautifulSoup(t, "lxml")
name = soup.find('table')
