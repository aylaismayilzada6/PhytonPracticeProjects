import requests
from twilio.rest import Client


#api_key = "6c6616301ec6bc0f894548c1ea11cee5"
api_key = "YOUR_API_KEY"

weather_end_point = "https://api.openweathermap.org/data/2.5/forecast"


account_sid = "YOUR_SID"
auth_token = "YOUR_TOKEN"


weather_params = {
    "lat":-16.9186,
    "lon":145.7781,
    "appid": api_key,
    "cnt": 4
}
response_w = requests.get(weather_end_point, params= weather_params)
response_w.raise_for_status()
weather_data = response_w.json()

will_rain = False

for hour_data in weather_data["list"]:
    weather_cond_id = hour_data["weather"][0]["id"]
    if int(weather_cond_id) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body="It's going to rain today. You can stay under my umbrella~~~~!",
        to='whatsapp:+994517671533'
    )
    print(message.status)
f