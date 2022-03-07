import requests

class Toggl:
    def __init__(self, token: str):
        self.token = token
        self.user_data = None

    
    def get_user_data(self):
        endpoint = "https://api.track.toggl.com/api/v8/me"

        params = {
            "with_related_data": "true"
        }

        response = requests.get(url=endpoint, auth=requests.auth.HTTPBasicAuth(self.token, 'api_token'), params=params)
        response.raise_for_status()

        return response.json()["data"]


    def get_tracked_time(self):
        endpoint = "https://api.track.toggl.com/reports/api/v2/summary"

        headers = {
            "Content-Type": "application/json",
        }

        params = {
            "user_agent": "jan@knorr.family",
            "workspace_id": 3570962,
            "client_ids": "45740780"
        }

        response = requests.get(url=endpoint, auth=requests.auth.HTTPBasicAuth(self.token, 'api_token'), params=params)

        # total_time = response.json()["total_grand"]

        return response.json()