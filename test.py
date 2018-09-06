from urllib import request as req
import json

route = input("What route: ").upper()
stop = input("What stop: ").upper()

def switch_demo(argument):
    switcher = {
        'A': '3164',
        'B': 4512,
        'B2': 4513,
        'C': 4515,
    }
    # (switcher.get(argument, "Invalid Route"))

route = (switch_demo(route))
print(route)

url = "https://www.broncoshuttle.com/Route/%s/Stop/%s/Arrivals?customerID=21" % (route, stop)


print(url)

response = req.urlopen("https://www.broncoshuttle.com/Route/4512/Stop/487169/Arrivals?customerID=21")
data = json.load(response)

print(response)

eta = data[0]["Minutes"]
eta = str(eta)

print(eta + " minutes until shuttle arrive")