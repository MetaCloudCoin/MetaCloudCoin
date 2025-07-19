import requests

def fetch_aws_ip_ranges():
    url = 'https://ip-ranges.amazonaws.com/ip-ranges.json'
    response = requests.get(url)
    return response.json()
