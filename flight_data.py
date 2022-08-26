import notification_manager


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, notification_flight_alarm):
        self. p = notification_flight_alarm
        print("test-", self.p)
        self.flight_detail(self.p)

    def flight_detail(self,p):

        for key, value in self.p.items():
            print(key, ':', value)

        notification_manager.NotificationManager(self.p)


