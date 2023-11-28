import requests

proxies = {
    'http': '91.144.77.20',
    'https': '91.144.77.20'
}

url = "https://httpbin.org/get" # response service
response = requests.get(url, proxies=proxies)

print(response.text)
