import certifi
import urllib3

http = urllib3.PoolManager(
	cert_reqs = 'CERT_REQUIRED',
	ca_certs = certifi.where()
	)

site = 'https://facebook.com' #site you want to test
try:
	r = http.request('GET',site)
	if r.status == 200:
		print("SSL is OK, site is accessable in your region")
	else:
		print(f"SSL Found, but there something wrong to access the website, {r.status}")
except:
	print("SSL is not found")