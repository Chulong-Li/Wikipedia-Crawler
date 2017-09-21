
# coding: utf-8

# In[1]:

import time
import urllib
from bs4 import BeautifulSoup
import requests

# @Author: Chulong Li


# In[2]:

start_url = "https://en.wikipedia.org/wiki/Food"
target_url = "https://en.wikipedia.org/wiki/Philosophy"


# In[3]:

def find_first_link(url):
    soup = BeautifulSoup(requests.get(url).text, "lxml")
    content = soup.find(id = "mw-content-text").find(class_ = "mw-parser-output")
    page_link = None
    for index in content.find_all("p", recursive = False):
        if (index.find("a", recursive = False)):
            page_link = index.find("a", recursive = False).get("href")
            break
    if not page_link:
        return
    first_link = urllib.parse.urljoin('https://en.wikipedia.org/', page_link)
    return first_link


# In[4]:

def web_crawl(history, target_url, max_step = 27):
    check = True
    if history[-1] == target_url:
        print("Congratulation! Philosophy Wikipedia page has been found.")
        check = False
    elif len(history) > max_step:
        print("Can't find Philosophy Wikipedia page: Searching page steps out of maximum. ")
        check = False
    elif history[-1] in history[:-1]:
        print("Can't find Philosophy Wikipedia page: Wikipedia pages duplicate.")
        check = False
    return check


# In[ ]:

page_list = [start_url]
while web_crawl(page_list, target_url):
    print("Wikipedia Crawler at " + page_list[-1])
    first_link = find_first_link(page_list[-1])
    if not first_link:
        print("Can't find Philosophy Wikipedia page: No links in this page.")
        break
    page_list.append(first_link)
    time.sleep(1)


# In[ ]:



