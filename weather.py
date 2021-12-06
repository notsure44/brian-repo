#!/Users/sdaniels/.pyenv/shims/python3
import sys
import requests

#http://api.weatherapi.com/v1/current.json?key=98acecba0026494aa06204227210412&q=Austin&aqi=no

WEATHER_API_KEY = "98acecba0026494aa06204227210412"

user_input = input("Choose city:\n1: Austin\n2: Chicago\n3: Tampa\n")

city = None

if user_input == "1":
	city = "Austin"
elif user_input == "2":
	city = "Chicago"
elif user_input == "3":
	city = "Tampa"
else:
	print("Not a valid selection.")
	sys.exit(1)

print("You selected " + city)

url = "http://api.weatherapi.com/v1/current.json?key=%s&q=%s&aqi=no"%(WEATHER_API_KEY, city)
responce = requests.get(url=url)

weather_dictionary = responce.json()

temp = weather_dictionary["current"]["temp_f"]
wind = weather_dictionary["current"]["wind_mph"]
feels = weather_dictionary["current"]["feelslike_f"]
print("The temperature in %s is %s F"%(city, temp))
print("The wind in %s is %s mph"%(city, wind))
print("Feels like the temperature in %s is %s F"%(city, feels))
#Faaag