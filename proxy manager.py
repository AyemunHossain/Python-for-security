import urllib3
proxy = urllib3.ProxyManager('http://localhost:3128/')
proxy.request('GET', 'http://google.com/')