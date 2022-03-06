import requests

URL = "https://api.track.toggl.com/reports/api/v2/details"

class Toggl:
    def __init__(self, token: str):
        self.token = token

    
    def toggl_request(self):
        endpoint = URL

        headers = {
            "Content-Type": "application/json",
            "api_token": self.token
        }

        body = {
            
        }