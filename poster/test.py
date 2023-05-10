import requests
json = {"themes": "12132342"}
r = requests.put('https://gpt-tool.ru/api/channels/1/update/', data=json)
print(r.status_code)