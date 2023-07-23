import requests
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "1234567890ABCD"  # Your tequila API


class FlightSearch:
    """
    A class to perform flight searches using the Kiwi/Tequila API.

    Before using this class, you need to create a free account on https://tequila-api.kiwi.com
    and obtain your Kiwi Tequila API key.

    Usage:
        1. Create an instance of the FlightSearch class.
        2. Call the `get_iata_code` method to retrieve the IATA code for a specific city.
        3. Call the `check_flight_deals` method to search for flight deals based on specific criteria.

    Attributes:
        TEQUILA_ENDPOINT (str): The base URL for the Kiwi/Tequila API.
        TEQUILA_API_KEY (str): Your Kiwi Tequila API key.

    Methods:
        get_iata_code(city_name: str) -> str:
            Retrieves the International Air Transport Association (IATA) code for a given city.

        check_flight_deals(departure_code: str, arrival_code: str, from_time: str, to_time: str) -> FlightData:
            Searches for flight deals based on the provided criteria.

    Note:
        This class requires the `requests` library to be installed.
        You can install it using the following command: `pip install requests`.
    """

    def get_iata_code(self, city_name):
        """
        Retrieves the International Air Transport Association (IATA) code for a given city.

        Args:
            city_name (str): The name of the city.

        Returns:
            str: The IATA code for the city.
                 If the city is not found, it will print an error message and return None.
        """

        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "airport"}

        try:
            response = requests.get(url=location_endpoint, headers=headers, params=query)
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(f"ERROR LOG: {err}")
        else:
            results = response.json()["locations"]
            return results[0]["code"]

    def check_flight_deals(self, departure_code, arrival_code, from_time, to_time):
        """
        Searches for flight deals based on the provided criteria.

        Args:
            departure_code (str): The IATA code of the departure city.
            arrival_code (str): The IATA code of the arrival city.
            from_time (str): The starting date for the search in the format "DD-MM-YYYY".
            to_time (str): The ending date for the search in the format "DD-MM-YYYY".

        Returns:
            FlightData: An object representing the flight data found in the search.
                        If no flights are found, it will print a log message and return None.
        """

        search_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": departure_code,
            "fly_to": arrival_code,
            "date_from": from_time,
            "date_to": to_time,
            "nights_in_dst_from": 10,
            "nights_in_dst_to": 30,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD"
        }

        response = requests.get(url=search_endpoint, headers=headers, params=query)
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"MSG Log: No flights found for {departure_code} to {arrival_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )

        print(f"MSG Log: From {flight_data.origin_airport} to {flight_data.destination_airport} - "
              f"USD{flight_data.price} \n"
              f"Departure Date: {flight_data.departure_date} - "
              f"Arrival Date: {flight_data.arrival_date}")

        return flight_data
