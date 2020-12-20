import urllib.request

url = "https://www.bing.com/search?q=python"
headers ={}
headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
req = urllib.request.Request(url, headers= headers)

data =urllib.request.urlopen(req)
print(data.read())