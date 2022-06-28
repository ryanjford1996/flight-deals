import requests

SHEETY_ENDPOINT = 'Sheety endpoint for Google Sheet'

class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        cutoff_costs = requests.get(url=SHEETY_ENDPOINT, headers=headers)
        cutoff_costs = cutoff_costs.json()
        return cutoff_costs['prices']

    def update_sheet(self):
        for city in self.destination_data:
            update = {
                'price':
                    {'iataCode': city['iataCode']}
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=update)
            print(response.text)