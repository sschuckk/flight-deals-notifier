class FlightData:
    """
    Represents flight data for a specific flight itinerary.

    Attributes:
        price (float): The price of the flight.
        origin_city (str): The name of the origin city for the flight.
        origin_airport (str): The IATA code of the origin airport for the flight.
        destination_city (str): The name of the destination city for the flight.
        destination_airport (str): The IATA code of the destination airport for the flight.
        departure_date (str): The departure date of the flight in the format "DD-MM-YYYY".
        arrival_date (str): The arrival date of the flight in the format "DD-MM-YYYY".

    Note:
        This class is used to structure and store flight data retrieved from flight searches.
        It does not have any methods other than the constructor (__init__).
    """

    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date):
        """
        Initializes a new instance of the FlightData class with the provided flight data.
        """

        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.departure_date = out_date
        self.arrival_date = return_date
