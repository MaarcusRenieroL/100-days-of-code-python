API_KEY="b6ad709512cc4c8a71758039e91d2f6e"
LAT=13.082680
LONG=80.270721
OWM_Endpoint="https://api.openweathermap.org/data/2.5/onecall"
weather_params={
    "lat":LAT,
    "lon":LONG,
    "appid":API_KEY,
    "exclude":"current, minutely, daily"
}
account_sid="AC9acc3f8c9a456cf708997528fe3b819f"
auth_token="8918e195b4eccb2b9993ee8d4a13c9ed"

import requests
from twilio.rest import Client

response=requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data=response.json()
hourly_weather=weather_data['hourly'][:12]
will_rain=False
for hour_data in hourly_weather:
    if int(hour_data['weather'][0]['id'])<700:
        will_rain=True
if will_rain:
    client=Client(account_sid, auth_token)
    message=client.messages.create(body="It's raining today. Have an ☔ with you", from_='+14232056730', to='+917299954472')
    print(message.status)
