import requests, re
from bs4 import BeautifulSoup

r = requests.get("http://webscraper.io/test-sites/e-commerce/allinone/phones").content
soup = BeautifulSoup(r, "lxml")

tags = soup.findall('a', {"href":re.compile("[<>#%|\{\}!\\^~\[\]`/]")})
for a in tags:
	print(a.get("href"))

r2 = requests.get("http://webscraper.io/test-sites/e-commerce/allinone/phones").content  
soup2 = BeautifulSoup(r, "lxml")  
tags2 = soup.findAll("div", {"class":re.compile('(ratings)')})  
for p in tags2:  
        a = p.findAll("p",{"class":"pull-right"})  
        print(a[0].string)  