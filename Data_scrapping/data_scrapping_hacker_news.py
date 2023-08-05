import requests
from bs4 import BeautifulSoup
import pprint

res= requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(res.text,"html.parser")
links= soup.select(".titleline")
subtext= soup.select(".subtext")

def sorting_fun(hnlist):
    return sorted(hnlist,key=lambda k:k["vote"],reverse=True)

def create_custom_hn(links,subtext):
    hn=[]
    for idx, item in enumerate(links):
        title= links[idx].getText()
        #href= links[idx].get("href",None)
        vote= subtext[idx].select(".score")
        if len(vote):
            points= int(vote[0].getText().replace(" points",""))
            if points >99:
                hn.append({"title":title, "vote":points})
    return sorting_fun(hn)
pprint.pprint(create_custom_hn(links,subtext))

 
 
 

