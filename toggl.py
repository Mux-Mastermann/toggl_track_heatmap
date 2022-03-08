import requests

class Toggl:
    def __init__(self, token: str):
        self.token = token
        self.workspace_id = None
        self.active_projects = None
        self.clients = None
        self.tags = None
        self.get_user_data()

    
    def get_user_data(self):
        """Gets all the user data from Toggl and sets the required attributes of the class based on this data"""
        endpoint = "https://api.track.toggl.com/api/v8/me"

        params = {
            "with_related_data": "true"
        }

        response = requests.get(url=endpoint, auth=requests.auth.HTTPBasicAuth(self.token, 'api_token'), params=params)
        response.raise_for_status()

        data = response.json()["data"]

        self.workspace_id = data["default_wid"]
        self.active_projects = [project for project in data["projects"] if project["wid"] == self.workspace_id and project["active"] and not project.get("server_deleted_at", False)]
        self.clients = [client for client in data["clients"] if client["wid"] == self.workspace_id]
        self.tags = [tag for tag in data["tags"] if tag["wid"] == self.workspace_id]


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