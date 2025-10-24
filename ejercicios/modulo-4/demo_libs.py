import requests

url = "https://api.github.com/users/google"

response = requests.get(url)

data = response.json()

print(data)