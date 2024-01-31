import requests
from .config import API_BASE_URL, ACCESS_TOKEN

class FootballApiClient:
    def __init__(self, api_base_url=API_BASE_URL, access_token=ACCESS_TOKEN):
        self.api_base_url = api_base_url
        self.access_token = access_token
        self.headers = {
            "X-Auth-Token": self.access_token,
        }

    def get_areas(self):
        url = f"{self.api_base_url}/v4/areas"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_teams(self):
        url = f"{self.api_base_url}/v4/teams"
        response = requests.get(url, headers=self.headers)
        return response.json()
    
    def get_team_by_id(self, team_id):
        url = f"{self.api_base_url}/v4/teams/{team_id}"
        response = requests.get(url, headers=self.headers)
        return response.json()
    
    def get_player_by_id(self, player_id):
        url = f"{self.api_base_url}/v4/persons/{player_id}"
        response = requests.get(url, headers=self.headers)
        return response.json()
    
    def get_competitions(self):
        url = f"{self.api_base_url}/v4/competitions"
        response = requests.get(url, headers=self.headers)
        return response.json()