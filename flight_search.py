import requests
from flight_data import FlightData
from datetime import date, timedelta


TEQUILA_API_KEY = 'Your Key'
TEQUILA_ENDPOINT = 'https://tequila-api.kiwi.com'
FROM_DATE = (date.today() + timedelta(days=1)).strftime('%d/%m/%Y')
TO_DATE = (date.today() + timedelta(days=60)).strftime('%d/%m/%Y')

class FlightSearch:
    def __init__(self):
        pass

    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def search_flight(self, depart_city_iata, destination_city_iata , price_to, from_date, to_date):
        parameters = {
            'fly_from': depart_city_iata,
            'fly_to': destination_city_iata,
            'date_from': from_date,
            'date_to': to_date,
            'curr': 'USD',
            'price_to': price_to,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
        }
        headers = {'apikey': TEQUILA_API_KEY}
        flight_info = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", params=parameters, headers=headers)
        try:
            data = flight_info.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_iata}")
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

        print(f"{flight_data.destination_city}: ${flight_data.price}")

        return flight_data
