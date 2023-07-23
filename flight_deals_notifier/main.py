"""
Flight Deal Notifier Script

This script searches for flight deals from a list of cities using APIs and notifies the user via SMS if a deal
is found with a price lower than the specified in a Google sheets doc.

Note: Before running this script, ensure that the necessary credentials and environment variables are properly
configured for accessing the Google Sheets, Sheety, and Twilio API.
"""

# Import the necessary modules
from flight_deals_notifier.commom.data_manager import DataManager
from flight_deals_notifier.commom.flight_search import FlightSearch
from flight_deals_notifier.commom.notifier_manager import NotificationManager

# Create instances of the required classes
flight_search = FlightSearch()
notifier_manager = NotificationManager()
data_manager = DataManager()
sheet_data = data_manager.get_sheet_data()

# Update Google Sheets with the IATA Code for each City without a code
for row in sheet_data:
    if row["cityOrigen"] != "" and row["origenCode"] == "":
        row["origenCode"] = flight_search.get_iata_code(row["cityOrigen"])
    if row["cityDestination"] != "" and row["destinationCode"] == "":
        row["destinationCode"] = flight_search.get_iata_code(row["cityDestination"])
data_manager.sheet_data = sheet_data
data_manager.update_iata_codes()

# Get the dates from data
start_date = sheet_data[0]["startDate"]
end_date = sheet_data[0]["endDate"]

# Search for the deals using Origin City vs Destination City
# The same City Origen will be used for each City Destination
for origen in sheet_data:
    if origen["cityOrigen"] != "":
        for destination in sheet_data:
            if origen["cityDestination"] != "":
                flight = flight_search.check_flight_deals(
                    origen["origenCode"],
                    destination["destinationCode"],
                    from_time=start_date,
                    to_time=end_date
                )

                # Send an SMS if the price returned is lower than the price in Google Sheets for each City Destination
                if flight is not None and flight.price < destination["lowestPrice"]:
                    notifier_manager.send_sms(
                        message=f"Low price ALERT! Only USD{flight.price} "
                                f"to fly from {flight.origin_city}-{flight.origin_airport} "
                                f"to {flight.destination_city}-{flight.destination_airport}, "
                                f"from {flight.departure_date} to {flight.arrival_date}.")
