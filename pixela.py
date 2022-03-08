import requests

URL = "https://pixe.la"

class Pixela:
    def __init__(self, username: str, token: str):
        self.username = username
        self.token = token


    def check_credentials(self):
        """check if username exists"""
        pass


    def get_graphs(self):
        """Get all graphs from the user"""
        endpoint = f"{URL}/v1/users/{self.username}/graphs"

        headers = {
            "X-USER-TOKEN": self.token
        }

        response = requests.get(url=endpoint, headers=headers)

        return response.json()


    def create_user(self):
        """creates user on pixela. Username and password were set when creating the Pixela class"""
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
        """returns the user profile on pixela as html page"""
        endpoint = f"{URL}@{self.username}"

        response = requests.get(url=endpoint)

        return response