import requests

url = "https://api.stagingeb.com/v1/contact_requests?page=1&limit=50"

headers = {
    "accept": "application/json",
    "X-Authorization": "l7u502p8v46ba3ppgvj5y2aad50lb9"
}

response = requests.get(url, headers=headers)

print(response.text)