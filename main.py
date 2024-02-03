import requests
import os
import json

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    os.makedirs('json_files', exist_ok=True)

    for i, item in enumerate(data, start=1):
        with open(f'json_files/post_{i}.json', 'w', encoding='utf-8') as file:
            json.dump(item, file, ensure_ascii=False, indent=4)
else:
    print(f"Ошибка при запросе: Статус код {response.status_code}")