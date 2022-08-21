from flight_search import FlightSearch
import datamanager999

sheety_list = datamanager999.city_visit_list  # -------loopcount
loop_count = (datamanager999.lines())

for n in range(loop_count):
    try:
        print((sheety_list(n)[0]), (sheety_list(n)[1]))
        FlightSearch((sheety_list(n)[0]), sheety_list(n)[1])
    except:
        print("ticket price to high")

# FlightSearch('TYO',2600)
# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager
# classes to achieve the program requirements.


# for i in range(6):
#     city_code = (datamanager999.city_visit_list(i)[0])
#     price_limit = (datamanager999.city_visit_list(i)[1])
#     flight_search.search(city_code, price_limit)
#     i += 1
