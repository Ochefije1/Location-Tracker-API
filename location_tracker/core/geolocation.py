import requests

phone_number = "1234567890"
api_key = "YOUR_OPEN_CAGE_API_KEY"
url = f"https://api.opencagedata.com/geocode/v1/json?key={api_key}&q={phone_number}"

response = requests.get(url)
data = response.json()

# Parse the data to extract location information
