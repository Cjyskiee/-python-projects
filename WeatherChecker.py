import requests

api_key = "API_KEY_HERE" #put your Activated Api Key 
base_Url = "BASE_URL_HERE" #UR base URL weather_data url

while True:


    city = input("What city:")

    response = requests.get(base_Url, params= { 
        #dict of the list for response var

            "q" : city,
            "appid" : api_key,
            "units" : "metric"
    })
    data = response.json() # collect all the response data through json.

    if data["cod"] == 200:
        print(f"City: {data["name"]}")
        print(f"Temperature: {data["main"]["temp"]} °C")
        print(f"Feels Like: {data["main"]["feels_like"]}")
        print(f"Humidity: {data["main"]["humidity"]}")
        print(f"Wind & Speed: {data["wind"]['speed']} m/s")
        print(f"Weather Description: {data["weather"][0]["description"]}")
    elif data["cod"] == "404":
        print("City not found!")
    else:
        print(f"Error: {data['message']}")

