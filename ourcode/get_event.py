import requests as rq
URL="http://go.wroclaw.pl/api/v1.0/categories/for-offers"

data=rq.get(URL)
print(data)



