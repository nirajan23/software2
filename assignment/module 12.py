
# Write a program that fetches and prints out a ..


import requests

request = "https://api.chucknorris.io/jokes/random"
try:
    response = requests.get(request)
    if response.status_code == 200:
        json_response = response.json()
        print(json_response["value"])

except requests.exceptions.RequestException as e:
    print("Request could not be completed.")

print("\n-------------------------------------")

###2   Familiarize yourself with the OpenWeather weather API at: https://open..........
import requests

municipality = input("To know the current weather condition:\nEnter Municipality: ")
key = "2212dfcb0ef8ca373f1b9601290b42c8"
request = f"https://api.openweathermap.org/data/2.5/weather?q={municipality}&appid={key}&units=metric"

try:
    response = requests.get(request)
    if response.status_code == 200:
        json_response = response.json()
        main = json_response['main']
        temperature = main['temp']
        humidity = main['humidity']
        report = json_response['weather']

except requests.exceptions.RequestException as e:
    print("Request could not be completed.")

print("\nThe corresponding weather condition of the entered location is:")
print(f"Temperature: {temperature:.2f} degree celsius")
print(f"Humidity: {humidity}")
print(f"Weather Report: {report[0]['description']}")