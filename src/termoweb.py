import httpx

class Termoweb:
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password

        self.termowebToken = "Basic NTIxNzJkYzg0ZjYzZDZjNzU5MDAwMDA1OmJ4djRaM3hVU2U="
        self.userToken = None

        self.baseUrl = "https://control.termoweb.net"

    def login(self):
        response = httpx.post(
            f'{self.baseUrl}/client/token',
            data = {
                'username': self.email,
                'password': self.password,
                'grant_type': 'password'
            },
            headers = {
            "Authorization": self.termowebToken
        })

        if response.status_code != 200:
            raise Exception(f"Login failed: {response.status_code} - {response.text}")
        self.userToken = response.json()['access_token']

