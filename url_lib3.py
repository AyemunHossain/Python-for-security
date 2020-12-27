import urllib3 as url
import json
http = url.PoolManager()

# request = http.request('GET','http://google.com')
# print(request.status)
# print(request.headers)

request = http.request('GET', 'http://httpbin.org/ip')
print(json.loads(request.data.decode('utf-8')))