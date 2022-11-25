import json
import requests

key = '265cc97a8fc6bb1b657b3969b673f19f'
format = 'text' 
url = "https://portulanclarin.net/workbench/lx-proficiency/api/"


text = '''
Olá, meu nome é Miguel, e eu venho dos Açores. Tenho 35 anos e sou engenheiro civil.
'''

request_data = {
    'method': 'analyse',
    'jsonrpc': '2.0',
    'id': 0,
    'params': {
        'text': text,
        'format': format,
        'key': key,
    },
}
request = requests.post(url, json=request_data)
response_data = request.json()
if "error" in response_data:
    print("Error:", response_data["error"])
else:
    print("Result:")
    print(response_data["result"].split("\n")[4][-2:])



# Getting acess key status:
request_data = {
    'method': 'key_status',
    'jsonrpc': '2.0',
    'id': 0,
    'params': {
        'key': key,
    },
}
request = requests.post(url, json=request_data)
response_data = request.json()
if "error" in response_data:
    print("Error:", response_data["error"])
else:
    print("Key status:")
    print(json.dumps(response_data["result"], indent=4))