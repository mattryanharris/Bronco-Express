from urllib import request as req
import json

route = input("What route: ").upper()
stop = input("What stop: ").upper()

if route == 'B':
	route = 4512

if stop == "RESIDENTS HALL":
	stop = 487169

if stop == "BUILDING 94":
	stop = 33803

if route == 'A':
	route = 3164

if stop == "OVERFLOW PARKING LOT":
	stop = 1592066

url = "https://www.broncoshuttle.com/Route/%s/Stop/%s/Arrivals?customerID=21" % (route, stop)

response = req.urlopen(url)
data = json.load(response)


eta = data[0]["Minutes"]
eta = str(eta)

print(eta + " minutes until shuttle arrive")