#!/usr/bin/env python

from bs4 import BeautifulSoup
from hashlib import md5
import requests

#soup = BeautifulSoup(open("out.html"), 'html.parser')
response = requests.get('http://forecast.weather.gov/MapClick.php?map.x=241&map.y=170&minlon=-121.29&maxlon=-117.61&minlat=32.65&maxlat=35.81&mapwidth=354&site=lox&zmx=1&zmy=1')
soup = BeautifulSoup(response.content, 'html.parser')
roi = soup.find(id="detailed-forecast-body")


#print roi.text
m = md5()
m.update(unicode(roi))
print m.hexdigest()
print roi
