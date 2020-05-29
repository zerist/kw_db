class Content:
    """page html base class"""

    def __init__(self, topic, url, title, body):
        self.topic = topic
        self.url = url
        self.title = title
        self.body = body

    def print(self):
        print("New article found for topic: {}".format(self.topic))
        print("Title: {}".format(self.title))
        print("Body: \n{}".format(self.body))
        print("Url: {}".format(self.url))



class Website:
    """web site basic class"""

    def __init__(self, name, url, searchUrl, resultListing, resultUrl, absoluteUrl, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.searchUrl = searchUrl
        self.resultListing = resultListing
        self.resultUrl = resultUrl
        self.absoluteUrl = absoluteUrl
        self.titleTag = titleTag
        self.bodyTag = bodyTag

