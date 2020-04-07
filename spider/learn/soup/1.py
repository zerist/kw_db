from urllib import request, error
from bs4 import BeautifulSoup as soup

def getTitle(url):
    try:
        html = request.urlopen(url)
    except error.HTTPError as e:
        return None

    try:
        bs = soup(html, 'html.parser')
        title = bs.title
    except AttributeError as e:
        return None

    return title

title = getTitle("http://www.baidu.com")
if title == None:
    print("Title not found")
else:
    print(title)
