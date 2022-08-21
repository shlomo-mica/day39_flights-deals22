import requests

 # class DataManager:
#     # This class is responsible for talking to the Google Sheet.
#     pass


API_LOCATION_KEY = "_JJjkemRSPqvR8hWOG34DSLAugfZU8wP"
END_POINT = "https://tequila-api.kiwi.com/locations/query/"
GET_CITY_NAME = ''


def city_code(a):
    """

    :rtype: airport iata code
    """
    headers = {"apikey": API_LOCATION_KEY}
    query = {"term": a}
    city_code1 = requests.get(url=END_POINT, headers=headers, params=query)
    sheety_city_code = city_code1.json()
    city_code1 = sheety_city_code["locations"][0]["code"]
    return city_code1


#   SHEETY AREA
# ---------------------------------------------------------------------------------------------------------------
def city_name(i):
    global get_flight_value, get_city_name

    end_point = f"https://api.sheety.co/71fa5adad7d23ff3514fc4b38242f901" \
                f"/flightDeals/prices/{i}"

    header = {"Authorization": "Bearer NeLi2022",
              'Content-Type': 'application/json'}
    response = requests.get(url=end_point, params=header)
    get_cityname = response.json()
    print(get_cityname)
    get_city_name = get_cityname['price']['city']
    get_flight_value = get_cityname['price']['lowestPrice']

    if get_cityname['price']['iataCode'] == ' ':
        body = {
            'price': {
                "iataCode": city_code(get_city_name)}}  # call the city code function and fill the empty sheet cell
        # "city": get_city_name} not necessary good for learning

        header2 = {"Authorization": "Basic c2hsb21vIG1pY2E6emFxMTJ3c3g=",
                   'Content-Type': 'application/json'}
        x = requests.put(url=end_point, params=header, json=body)

    else:
        # print("cells are filled")
        return get_city_name, get_flight_value

