import requests
import os

class SpotifyAPI:
    def __init__(self, client_id, client_secret, user_id):
        self.client_id = client_id
        self.client_secret = client_secret
        self.user_id = user_id
        self.BASE_URL = "https://api.spotify.com/v1"

    def _get_auth_token(self):
        auth_url = "https://accounts.spotify.com/api/token"
        auth_data = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }
        auth_response = requests.post(auth_url, data=auth_data)
        return auth_response.json()["access_token"]

    def get_user_data(self):
        token = self._get_auth_token()
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(f"{self.BASE_URL}/users/{self.user_id}", headers=headers)
        return response.json()
