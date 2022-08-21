import requests
import datamanager999
from datetime import timedelta, datetime

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "EE--B8Y0SnG2mc0VJSHuAhVHQi8TgXmV"
tomorrow_datetime = datetime.now() + timedelta(days=1)
six_month = tomorrow_datetime + timedelta(days=6 * 365 / 12)


#     # This class is responsible for talking to the Flight Search API.
class FlightSearch:
    def __init__(self, city_code1, flight_cost1=int):
        self.code = city_code1
        self.flight_cost = flight_cost1
        self.search()

    def search(self):
        headers = {"apikey": TEQUILA_API_KEY}

        query = {
            "fly_from": 'LON',
            "fly_to": self.code,
            "date_from": tomorrow_datetime.strftime("%d/%m/%Y"),
            "date_to": six_month.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,  # 0 FOR DIRECT FLIGHTS ONLY
            "curr": 'GBP',
            'price_to': self.flight_cost
        }
        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=headers,
            params=query)

        flight_price = (response.json()["data"])  # list
        #print(flight_price)

        print(flight_price[0]['id'])
        print(flight_price[0]['flyTo'])
        print(flight_price[0]['price'])
        route_count = len(flight_price[0]['route'])

        for i in range(route_count):
            print(flight_price[0]['route'][i]['id'])
            print(flight_price[0]['route'][i]['operating_flight_no'])
            print(flight_price[0]['route'][i]['local_departure'])
            i += 1



# print(to_time.strftime("%d/%m/%Y"))
# to_time = datetime(2022, 12, 4)
# flyto22=input("city code ??").upper()
# fly_cost22=input("fly cost ??").upper()
# flyto = datamanager999.city_visit_list(city1)[0]
# fligh_cost = datamanager999.city_visit_list(price1)[1]
