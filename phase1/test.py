import requests
from pprint import pprint
key = "14a85395c35f4bfe95c47de3ff21edae"
url = "https://api.football-data.org/v2/competitions/MLS"
response = requests.get(url, headers={"X-Auth-Token":key})
pprint(response.json())