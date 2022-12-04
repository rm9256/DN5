import requests
import json

def get_api_data(url):
    r = requests.get(url)
    returnCode = r.status_code
    if returnCode == 200:
        #print(type(r))
        slovar = json.loads(r.text)
        return slovar
    else:
        return False
#page = get_api_data("https://jsonplaceholder.typicode.com/nedala/nedala")
#print(page)