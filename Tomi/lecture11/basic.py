import requests
from requests.exceptions import Timeout
# from requests.exceptions import HTTPError
# try:
#   response = requests.get('https://example.com/ndjsdnl')
#   response.raise_for_status()
# except HTTPError as http_error:
#   print('fail', http_error)
# except Exception as err:
#   print(err)
# else:
#   print('success')

# response = requests.get('https://api.github.com/search/repositories', params=[('q', 'requests+language:python')],
#   headers={ 'Accept': 'application/json' }
# )
# response.encoding = 'utf-8'
# print(response.headers)

# requests.put('https://', data=[('key', 'value')])
# requests.put('https://', json={'key': 'value'})
# try:
#   response = requests.post('https://example.com', timeout=(2, 0.1))
#   print(response.status_code)
# except Timeout:
#   print('timeout')
# else:
#   print('success')

with requests.Session() as session:
  session.auth = ('username', 'password')

  session.get()
