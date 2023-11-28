import requests

headers = {
    "User-Agent": "Mobile", # user agents serve based on device and interface like a browser
    "Accept": "image/png" # accept image/png
}
url = "https://httpbin.org/image" # response service
response = requests.get(url, headers=headers)
# you can also timeout requests by adding a timeout parameter to the get() function

with open("image.png", "wb") as file:
    file.write(response.content)

# if response.status_code == 200: #/user-agent
#     data = response.json()
#     print(data)
# else:
#     print("Request failed with status code:", response.status_code)
