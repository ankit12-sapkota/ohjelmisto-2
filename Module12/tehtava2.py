import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
weather_api = os.getenv("weather_api")


municipality = input("Enter the name of your municipality. ")

long_latitude = f"http://api.openweathermap.org/geo/1.0/direct?q={municipality} &limit={1}&appid={weather_api}"


try:
    response = requests.get(long_latitude)
    if response.status_code==200:
            response_json = response.json()
            
            
            latitude = response_json[0]["lat"]
            longitude = response_json[0]["lon"]
            print(longitude, latitude)
            
  
  
except requests.exceptions.RequestException as e:
    print ("Request could not be completed.")


weather_request = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={weather_api}"

try:
     result = requests.get(weather_request)
     if response.status_code==200:
          result_json = result.json()
          #print(json.dumps(result_json, indent=2))
          description = result_json["weather"][0]["description"]
          temperature_kelvin = result_json["main"]["temp"]
          print(description, temperature_kelvin)


except requests.exceptions.RequestException as e:
     print("Request could not be completed.")       

celcius = round(temperature_kelvin - 273.15)

print(f"Temperature of {municipality}: {celcius} celcius.")
print(f"Weather description: {description}")
