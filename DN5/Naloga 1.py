import requests
def get_html(url):
    r = requests.get(url)
    returnCode = r.status_code
    if returnCode == 200:
        return r.text
    else:
        return False
#page = get_html("https://example.com/neobstaja")
#print(page)