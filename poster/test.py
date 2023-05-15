import requests
json = {"themes": "121323f42"}
r = requests.put('https://gpt-tool.ru/api/channels/1/update/', data=json)
print(r.status_code)