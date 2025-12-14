import os

from amadeus import Client, ResponseError
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

AMADEUS_CLIENT_ID = os.getenv("AMADEUS_CLIENT_ID")
AMADEUS_CLIENT_SECRET = os.getenv("AMADEUS_CLIENT_SECRET")

# Initialize Amadeus client
amadeus = Client(client_id=AMADEUS_CLIENT_ID, client_secret=AMADEUS_CLIENT_SECRET)


def search_flights(origin: str, destination: str, date: str, adults: int = 1):
    """
    Search for flights using the Amadeus API.
    Returns a list of flight offers or empty list if error occurs.
    """
    try:
        response = amadeus.shopping.flight_offers_search.get(
            originLocationCode=origin,
            destinationLocationCode=destination,
            departureDate=date,
            adults=adults,
        )
        return response.data
    except ResponseError as e:
        print(f"Amadeus API error: {e}")
        return []


if __name__ == "__main__":
    # Example usage
    flights = search_flights("MAD", "BOS", "2024-12-25")
    print(flights)
