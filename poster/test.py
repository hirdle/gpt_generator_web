j = {"telegram_id": -1001856652818, "owner": 1}
import requests
r = requests.put(f'http://gpt-tool.ru/api/channels/2/update/', data=j)
print(r.json())