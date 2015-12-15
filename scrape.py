#!/usr/bin/env python

from hashlib import md5
import requests
from time import gmtime, strftime

from bs4 import BeautifulSoup
import sqlite3

#soup = BeautifulSoup(open("out.html"), 'html.parser')

ts = strftime("%Y-%m-%d %H:%M:%S", gmtime())


response = requests.get('http://forecast.weather.gov/MapClick.php?map.x=241&map.y=170&minlon=-121.29&maxlon=-117.61&minlat=32.65&maxlat=35.81&mapwidth=354&site=lox&zmx=1&zmy=1')
soup = BeautifulSoup(response.content, 'html.parser')
roi = soup.find(id="detailed-forecast-body")


#print roi.text
m = md5()
m.update(unicode(roi))
digest =  m.hexdigest()


conn = sqlite3.connect('noaa_sm_bay.db')
cur = conn.cursor()

# if db file doesn't exist, create
try:
    cur.execute('''CREATE TABLE scrape
    (ts text, digest text, forecast text)''')
except sqlite3.OperationalError:
    pass # table already exists

# get most recent entry and see if hash digest is the same
cur.execute("SELECT digest from scrape order by ts desc;");
test_digest = cur.fetchone()[0]

print digest, test_digest
if digest != test_digest:
    cur.execute("INSERT INTO scrape VALUES (?, ?, ?);", (ts, digest, unicode(roi)))
    print digest
    print roi
else:
    print "no change"
#import pdb; pdb.set_trace()

conn.commit()
conn.close()
# Insert a row of data
