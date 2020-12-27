from urllib.parse import urlencode
import json
import urllib3 as url
http = url.PoolManager()


encoded_args = urlencode({'arg': 'value'})
url = 'http://httpbin.org/post?' + encoded_args
r = http.request('POST', url)
print(json.loads(r.data.decode('utf-8'))['args'])