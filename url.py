# used to parse values into the url
import urllib.parse
import urllib.request
import re

url = "http://econpy.pythonanywhere.com/ex/001.html"

# ages = re.findall(r'\d{1}',exampleString)
# names = re.findall(r'[f][a-z]^',exampleString)

req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
respData = resp.read()

buyerName = re.findall(r'<div title="buyer-name">(.*?)</div>', str(respData))
prices = re.findall(r'<span class="item-price">(.*?)</span><br>', str(respData))

print(buyerName)
print(prices)