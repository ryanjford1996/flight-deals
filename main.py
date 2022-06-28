from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import date, timedelta


FROM_DATE = (date.today() + timedelta(days=1)).strftime('%d/%m/%Y')
TO_DATE = (date.today() + timedelta(days=180)).strftime('%d/%m/%Y')
DEPART_CITY_IATA = 'your departure airport IATA code'

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

if sheet_data[0]['iataCode'] == '':
    for row in sheet_data:
        row['iataCode'] = flight_search.get_destination_code(row['city'])
    print(sheet_data)
    data_manager.destination_data = sheet_data
    data_manager.update_sheet()

for row in sheet_data:
    flight = flight_search.search_flight(DEPART_CITY_IATA, row['iataCode'], row['lowestPrice'], FROM_DATE, TO_DATE)
    if flight == None:
        pass
    elif flight.price < row['lowestPrice']:
        message = f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to" \
                  f" {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to " \
                  f"{flight.return_date}."
        notification_manager.send_emails(message)