import requests
from datetime import datetime

LAT=51.587351
LNG=-0.127758

# response=requests.get(url="http://api.open-notify.org/iss-now.json")

# response.raise_for_status()

# data=response.json()

# print(data["iss_position"]["longitude"], data["iss_position"]["latitude"])

parameters={
    "lat":LAT,
    "lng":LNG,
    "formatted":0
}
response=requests.get(f"https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data=response.json()
sunrise=data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset=data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise, sunset)