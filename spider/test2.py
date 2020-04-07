import requests
import json
from bs4 import BeautifulSoup

#参数设置
TIME_OUT = 3
HEADERS = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'Cookie': 'JSESSIONID=37C16FBA1C68E484FEAA0DBB3957C55D',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'pcdb.wbgcas.cn',
    'Referer': 'http://pcdb.wbgcas.cn/page/showEntity.vpage?uri=cn.csdb.whbgip.plantpic',
    'X-CSRF-TOKEN': 'f3b98b97-c101-4b0c-9ee3-8e33f86c38f1',
}


#爬取网站
MAIN_URL = "http://pcdb.wbgcas.cn/page/showEntity.vpage?uri=cn.csdb.whbgip.plantpic#"
BASE_URL = "http://pcdb.wbgcas.cn/"

test_url = "http://pcdb.wbgcas.cn/!doQuery.vpage"
#请求
post_data = {
    'query': '%257B%2522entity%2522%253A%2522cn.csdb.whbgip.plantpic%2522%252C%2522whereFilter%2522%253Anull%252C%2522pageIndex%2522%253A1%252C%2522pageSize%2522%253A8%252C%2522orderField%2522%253A%2522%2522%252C%2522orderAsc%2522%253A%2522desc%2522%252C%2522variables%2522%253A%257B%257D%257D',
    'timestamp': '1586104280894',
    'seqid': 597
}

res = requests.post(test_url, headers=HEADERS, data=json.dumps(post_data))
html = res.text
print(html)



