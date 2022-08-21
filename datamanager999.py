import requests

global row_numbers

end_point = f"https://api.sheety.co/71fa5adad7d23ff3514fc4b38242f901" \
            f"/flightDeals/prices/"

header = {"Authorization": "Bearer NeLi2022",
          'Content-Type': 'application/json'}
response = requests.get(url=end_point, params=header)
get_cityname = response.json()


def city_visit_list(city_number):

    city_code = get_cityname['prices'][city_number]['iataCode']
    flight_price = get_cityname['prices'][city_number]['lowestPrice']
    return city_code, flight_price


def lines():
    # city_visit_list(0)
    row_numbers = len(get_cityname['prices'])
    return row_numbers
