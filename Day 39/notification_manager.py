from twilio.rest import Client

TWILIO_SID = "AC943c5f04b823ada48168e5ee93a49b4d"
TWILIO_AUTH_TOKEN = "71d0df295aa0bd14e605d150d2b07e43"
TWILIO_VIRTUAL_NUMBER = "+13306321596"
TWILIO_VERIFIED_NUMBER = "+917299954472"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
