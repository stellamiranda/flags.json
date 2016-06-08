#!/usr/bin/env python
#coding: utf-8

import requests
from bs4 import BeautifulSoup
import collections
import json

url = 'https://en.wikipedia.org/wiki/Gallery_of_sovereign_state_flags'
resp = requests.get(url)
soup = BeautifulSoup(resp.content, 'lxml')

div = soup.find(id='mw-content-text')

flags = collections.defaultdict(dict)
for anc in div.findAll('a'):
        img_object = anc.find('img')
        if img_object:
            img_thumb = "https:" + img_object.attrs["src"]
            img = "/".join(img_thumb.replace("thumb/", "").split("/")[:-1])
            title = img_object.attrs["alt"]
            country = title.split('of')[-1].strip()
            flags[country] = {'flag': img, 'flag_thumb': img_thumb, 'cn_name': ''}

print json.dumps(flags, indent=4)
