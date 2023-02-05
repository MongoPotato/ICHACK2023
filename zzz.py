"""
import requests

url = "https://api.tryterra.co/v2/subscriptions"

headers = {
    "accept": "application/json",
    "dev-id": "testingTerra",
    "x-api-key": "ussv5SAQ53a1nNTxsMr9G41zj2KUhYMk5eDU1hjG"
}

response = requests.get(url, headers=headers)

print(response.text)

"""
import requests

url = "https://api.tryterra.co/v2/auth/generateWidgetSession"

payload = {
    "reference_id": "Brian",
    "providers": "GARMIN,WITHINGS,FITBIT,GOOGLE,OURA,WAHOO,PELOTON,ZWIFT,TRAININGPEAKS,FREESTYLELIBRE,DEXCOM,COROS,HUAWEI,OMRON,RENPHO,POLAR,SUUNTO,EIGHT,APPLE,CONCEPT2,WHOOP,IFIT,TEMPO,CRONOMETER,FATSECRET,NUTRACHECK,UNDERARMOUR",
    "language": "en"
}
headers = {
    "accept": "application/json",
    "dev-id": "testingTerra",
    "content-type": "application/json",
    "x-api-key": "ussv5SAQ53a1nNTxsMr9G41zj2KUhYMk5eDU1hjG"
}

response = requests.post(url, json=payload, headers=headers)
response.raise_for_status()

url = response.json()["url"]

print(url)

