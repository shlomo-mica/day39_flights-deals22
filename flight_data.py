
class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, notification_light_alarm):
        self.p = notification_light_alarm
        print("test-", notification_light_alarm.key)
