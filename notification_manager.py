from twilio.rest import Client

account_sid = 'AC3179819aa6c7d841526cae8d1bc0d360'
auth_token = "fdb3c6828f88887c264f02016ecb4baf"
client = Client(account_sid, auth_token)
# # This class is responsible for sending notifications with the deal flight details.


class NotificationManager:

    def __init__(self, q_text=dict):
        self.text = q_text
        self.sent_function(self.text)

    def sent_function(self, h):
        message = client.messages \
            .create(
            body=h,
            from_='+13512478114',
            # to='+15558675310'
            to='+972525698368'
        )
        print(message.sid)


