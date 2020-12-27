import urllib3 as url 
import json
http = url.PoolManager()

r = http.request(
    'POST',
    'http://httpbin.org/post',
    fields={'field': 'value'})

print(json.loads(r.data.decode('utf-8')))