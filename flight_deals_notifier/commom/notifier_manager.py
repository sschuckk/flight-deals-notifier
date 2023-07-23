import os
from twilio.rest import Client
from dotenv import load_dotenv

# Load env credentials
load_dotenv()
twilio_sid = os.getenv('TWILIO_SID')  # Your Twilio account SID
twilio_auth_token = os.getenv('TWILIO_AUTH_TOKEN')  # Your Twilio token
twilio_virtual_number = os.getenv('TWILIO_VIRTUAL_NUMBER')  # Your Twilio virtual number created
twilio_verified_number = os.getenv('TWILIO_VERIFIED_NUMBER')  # Your phone number verified by Twilio


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
        twilio_sid (str): Your Twilio account SID.
        twilio_auth_token (str): Your Twilio authentication token.
        twilio_virtual_number (str): Your Twilio virtual number from which the SMS will be sent.
        twilio_verified_number (str): Your phone number verified by Twilio.

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

        self.client = Client(twilio_sid, twilio_auth_token)

    def send_sms(self, message):
        """
        Sends an SMS notification with the given message.

        Args:
            message (str): The content of the SMS message.
        """

        message = self.client.messages.create(
            from_=twilio_virtual_number,
            to=twilio_verified_number,
            body=message
        )
        print(f"MSG Log: SMS sent token: {message.sid}")  # print if successfully sent.
