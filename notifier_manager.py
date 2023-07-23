from twilio.rest import Client

TWILIO_SID = "ABCDEFGHIJLMNOPQ123"  # Your Twilio account SID
TWILIO_AUTH_TOKEN = "1234567890ABCD"  # Your Twilio token
TWILIO_VIRTUAL_NUMBER = "+15551234567"  # Your Twilio virtual number created
TWILIO_VERIFIED_NUMBER = "+15557654321"  # Your phone number verified by Twilio


class NotificationManager:
    """
    A class to handle sending SMS notifications using Twilio API.

    Before using this class, you need to create a free Twilio account at https://www.twilio.com/
    and obtain your Twilio account SID, Twilio token, Twilio virtual number, and your phone number
    verified by Twilio.

    Usage:
        1. Create an instance of the NotificationManager class.
        2. Call the `send_sms` method with the desired message to send an SMS notification.

    Attributes:
        TWILIO_SID (str): Your Twilio account SID.
        TWILIO_AUTH_TOKEN (str): Your Twilio authentication token.
        TWILIO_VIRTUAL_NUMBER (str): Your Twilio virtual number from which the SMS will be sent.
        TWILIO_VERIFIED_NUMBER (str): Your phone number verified by Twilio.

    Methods:
        send_sms(message: str) -> None:
            Sends an SMS notification using the Twilio API.

    Note:
        This class requires the `twilio` library to be installed.
        You can install it using the following command: `pip install twilio`.
    """

    def __init__(self):
        """
        Initializes the NotificationManager with the Twilio client using the provided credentials.
        """

        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        """
        Sends an SMS notification with the given message.

        Args:
            message (str): The content of the SMS message.
        """

        message = self.client.messages.create(
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
            body=message
        )
        print(f"MSG Log: SMS sent: {message.sid}")  # print if successfully sent.
