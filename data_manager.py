import requests

SHEETY_ENDPOINT = "https://api.sheety.co/a429f8731234567890ABCD3890957fd9c2/flightDeals/prices"


class DataManager:
    """
    A class to manage and interact with data using Sheety API.

    Before using this class, you need to create a free account on https://sheety.co/
    and obtain the appropriate endpoint for your Google Sheet.

    Usage:
        1. Create an instance of the DataManager class.
        2. Call the `get_sheet_data` method to retrieve data from the Sheety API.
        3. Call the `update_iata_codes` method to update IATA codes for each city without one.

    Attributes:
        SHEETY_ENDPOINT (str): The API endpoint for the Sheety service.

    Methods:
        get_sheet_data() -> dict:
            Retrieves data from the Sheety API.

        update_iata_codes() -> None:
            Updates IATA codes for destinations in the Sheety API.

    Note:
        This class requires the `requests` library to be installed.
        You can install it using the following command: `pip install requests`.
    """

    def __init__(self):
        """
        Initializes the DataManager with an empty dictionary to store destination data.
        """

        self.sheet_data = {}

    def get_sheet_data(self):
        """
        Retrieves data from the Google Sheet using Sheety API.

        Returns:
            dict: A dictionary containing the retrieved data.
        """
        response = requests.get(url=SHEETY_ENDPOINT)
        data = response.json()
        self.sheet_data = data["prices"]
        return self.sheet_data

    def update_iata_codes(self):
        """
        Updates IATA codes for destinations in the Sheety API.
        """

        for city in self.sheet_data:
            new_data = {
                "price": {
                    "origenCode": city["origenCode"],
                    "destinationCode": city["destinationCode"]
                }
            }
            requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=new_data)
