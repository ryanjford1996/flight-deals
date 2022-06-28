from twilio.rest import Client
import requests
import smtplib
import os

MY_EMAIL = "your email here"
MY_PASS = "your password here"

SHEETY_URL = 'Sheety endpoint for Users sheet'

TWILIO_ACCOUNT_SID = 'Your SID'
TWILIO_AUTH_TOKEN = 'Your auth token'
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

class NotificationManager:
    def __init__(self):
        pass

    def send_message(self, message):
        message = client.messages \
            .create(
                body=message,
                from_='',
                to='',
        )
        print(message.sid)

    def send_emails(self, message):
        response = requests.get(SHEETY_URL)
        response = response.json()
        email_list = [x['email'] for x in response['users']]
        for email in email_list:
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASS)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:Good Flight Deal\n\n{message}"
                )