#!/usr/bin/env python

from bs4 import BeautifulSoup
from hashlib import md5

soup = BeautifulSoup(open("out.html"), 'html.parser')
roi = None
for x in soup.find_all('div'):
  # if "class" in x.attrs and "row-forecast" in x['class']:
  #   print x.get_text()
  if "id" in x.attrs and "detailed-forecast-body" in x['id']:
    #print x.get_text()
    #print x.head
    roi = x
    break

m = md5()
m.update(roi.text)
m.digest()
