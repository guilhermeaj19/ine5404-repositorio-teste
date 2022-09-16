import json
from urllib.error import URLError
import requests
import Exception
from aaa import checkData

url = 'https://jsonplaceholder.typicode.com/users'
try:

    res = requests.get(url)
    if res.status_code != 200:
        raise URLError('URL inválida', res.status_code)
    dados = json.loads(res.content)
    
except URLError as e:
    print(e)


for pessoa in dados:
    print(pessoa)
    print(checkData(pessoa))