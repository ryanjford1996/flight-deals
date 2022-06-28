import requests

SHEETY_URL = "Sheety endpoint for Users sheet"


class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def add_to_sheet(self):
        data = {
            "user": {
                "firstName": self.first_name,
                "lastName": self.last_name,
                "email": self.email,
            }
        }
        response = requests.post(url=SHEETY_URL, json=data)
        print(response.text)


first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
email = input("What is your email address?\n")
check_email = input("Please retype your email address.\n")

if email == check_email:
    new_user = User(first_name, last_name, email)
    new_user.add_to_sheet()