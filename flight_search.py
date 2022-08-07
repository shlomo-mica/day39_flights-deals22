import requests

from datetime import timedelta, datetime


TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "_JJjkemRSPqvR8hWOG34DSLAugfZU8wP"
tomorrow_datetime = datetime.now() + timedelta(days=1)
#TODO-1 6 MONTHES FROM TOMMOROW
to_time = datetime(2022, 12, 4)
headers = {"apikey": TEQUILA_API_KEY,
           'Content-Type': 'application/json'}
quary = {
    "fly_from": 'LON',
    "fly_to": 'PAR',
    "date_from": tomorrow_datetime.strftime("%d/%m/%Y"),
    "date_to": to_time.strftime("%d/%m/%Y"),
    "nights_in_dst_from": 7,
    "nights_in_dst_to": 30,
    "flight_type": "round",
    "one_for_city": 1,
    "max_stopovers": 0,
    "curr": "GBP",
    'price_to':''
#TODO-2 PRICE TAKEN FROM SHEETY TABLE DESTINATION>>>>>data_manager.py
}

response = requests.get(
    url=f"{TEQUILA_ENDPOINT}/v2/search",
    headers=headers,
    params=quary)
flight_price=response.json()
print(flight_price['data'][0]['price'])
print(flight_price)



class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    pass
