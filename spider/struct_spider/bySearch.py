import requests
from models import Content, Website
from bs4 import BeautifulSoup

class Crawler:

    def getPage(self, url):
        print(url)
        try:
            req = requests.get(url)
        except:
            return None
        return BeautifulSoup(req.text, 'html.parser')

    def safeGet(self, pageObj, selector):
        childObj = pageObj.select(selector)
        if childObj is not None and len(childObj) > 0:
            return childObj[0].get_text()
        return ""

    def search(self, topic, site):
        bs = self.getPage(site.searchUrl + topic)
        searchResults = bs.select(site.resultListing)
        for result in searchResults:
            url = result.select(site.resultUrl)[0].attrs["href"]
            if(site.absoluteUrl):
                bs = self.getPage(url)
            else:
                bs = self.getPage(site.url + url)
            if bs is None:
                print("page or url wrong!")
                return
            title = self.safeGet(bs, site.titleTag)
            body = self.safeGet(bs, site.bodyTag)
            if title != "" and body != "":
                content = Content(topic, title, body, url)
                content.print()

crawler = Crawler()

siteData = [
    ["Oreilly Media", 'http://oreilly.com', 'https://ssearch.oreilly.com/?q=', 'article.product-result','p.title a',True, 'h1', 'section#product-description']
]

sites = []
for row in siteData:
    sites.append(Website(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
topics = ['python', 'data science']
for topic in topics:
    print("Get info about: " + topic)
    for targetSite in sites:
        crawler.search(topic, targetSite)