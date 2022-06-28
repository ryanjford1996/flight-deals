# flight-deals
This application acquires customers, placing their information in a Google sheet using Sheety API. 

It then gets a dictionary of flight departure and destination locations as well as flight cost cutoffs and runs these against Tequila API, checking if a flight is available that is less than the given cutoff cost. 

If one of these flights is an acceptable cost, this application will send a text via Twilio or  an email via SMTP to alert the subscriber.
