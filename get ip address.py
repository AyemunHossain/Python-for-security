import urllib3 as url

http = url.PoolManager()

request = http.request('GET', 'http://httpbin.org/ip')
print(request.data)