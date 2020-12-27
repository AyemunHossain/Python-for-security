import urllib3
import json
http = urllib3.PoolManager()

with open('example.txt') as fp:
    file_data = fp.read()
r = http.request(
	'POST',
    'http://httpbin.org/post',
    fields ={'filefield':('example.txt',file_data)})

print(json.loads(r.data.decode('utf-8'))['files'])