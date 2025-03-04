import requests

url = "https://v3.football.api-sports.io/leagues"

payload={}
headers = {
  'x-rapidapi-key': 'be57b04cba0af2b105d88551e7f1093f',
  'x-rapidapi-host': 'v3.football.api-sports.io'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
