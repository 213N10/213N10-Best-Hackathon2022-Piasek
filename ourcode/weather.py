import requests as rq
from json import loads
URL='https://danepubliczne.imgw.pl/api/data/synop'

response=rq.get(URL)

omon=response.text
for line in loads(response.text):
    if line["stacja"]=="Wrocław":
        print(line)