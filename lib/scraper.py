from turtle import ht
from bs4 import BeautifulSoup
import requests

headers = {'user-agent': 'my-app/0.0.1'}
html = requests.get("https://flatironschool.com/", headers=headers)

doc = BeautifulSoup(html.text, 'html.parser');

print(doc);

print(doc.select('.visually-hidden')[0].contents);#heading-financier

#.heading-25-extrabold

mytitleobjs = doc.select('.heading-25-extrabold');

print(mytitleobjs);

#len(mytitleobjs)
for n in range(4):
    #print(mytitleobjs[n]);
    #print(mytitleobjs[n].contents);
    print(mytitleobjs[n].contents[0].strip());
    #print(type(mytitleobjs[n].contents[0]));
    #print(mytitleobjs[n].contents.strip);

print(mytitleobjs[0].name);
print(mytitleobjs[0].attrs);
