import requests

session = requests.session()
session.proxies = {
    'http': 'socks5h://localhost:9150',
    'https': 'socks5h://localhost:9150'}

print('requesting site')
r = session.get('http://nzxj65x32vh2fkhk.onion/all')
print(r.status_code)