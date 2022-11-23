import requests
from twilio.rest import Client


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
OWM_api_key = "b8e4f04ca46b7399411208aea410ef7c"
account_sid = "ACf7f58f8434c3757907a1c067a0f08e53"
account_authtoken = "0f18235f298b02f0d1351808e844b730"
Phone_Number = "+917990566879"

parameters = {
    "lat": 21.1598,
    "lon": 72.7959,
    "appid": OWM_api_key,
    "exclude": "alerts,current,minutely,daily"
}
response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
hourly_data = response.json()["hourly"]


will_rain = False
working_hours = hourly_data[:12]
for hour in working_hours:
    weather_code = hour["weather"][0]["id"]
    if weather_code < 600:
        will_rain = True
if will_rain:
    twilio_client = Client(account_sid, account_authtoken)
    message = twilio_client.messages.create(
        body="Don't forget to take the ☂ with you today!",
        from_='+14156049248',
        to=Phone_Number
    )

    print(message.status)
