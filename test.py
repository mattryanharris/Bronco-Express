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

print(route)

url = "https://www.broncoshuttle.com/Route/%s/Stop/%s/Arrivals?customerID=21" % (route, stop)

print(url)

response = req.urlopen(url)
data = json.load(response)

print(response)

eta = data[0]["Minutes"]
eta = str(eta)

print(eta + " minutes until shuttle arrive")