import requests

URL = "https://pixe.la"

class Pixela:
    def __init__(self, username: str, token: str):
        self.username = username
        self.token = token


    def create_user(self):
        endpoint = f"{URL}/v1/users"

        body = {
            "token": self.token,
            "username": self.username,
            "agreeTermsOfService": "yes",
            "notMinor": "yes"
        }

        response = requests.post(url=endpoint, json=body)
        status = response.status_code
        success = response.json()["isSuccess"]
        message = response.json()["message"]
        
        return status, success, message


    def get_user_profile(self):
        endpoint = f"{URL}@{self.username}"

        response = requests.get(url=endpoint)

        return response.status_code