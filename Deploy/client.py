from urllib import request
import os
os.environ['http_proxy'] = ''
URL='http://localhost:8000/'
response=request.urlopen(URL)
print(response.__dict__)
