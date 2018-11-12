import os

import requests

session = requests.session()
session.proxies = {}
session.proxies['http'] = os.getenv('http_proxy', 'socks5h://127.0.0.1:9050')
session.proxies['https'] = os.getenv('https_proxy', 'socks5h://127.0.0.1:9050')

print('requesting site')
r = session.get('http://nzxj65x32vh2fkhk.onion/all')
print(r.status_code)
