from urllib import request
import http.cookiejar

#如何使用cookie
url = 'http://www.ithome.com'
cj = http.cookiejar.CookieJar()
opener = request.build_opener(request.HTTPCookieProcessor(cj))
request.install_opener(opener)
response3 = request.urlopen(url)
print(response3.getcode())
print(cj)
print(response3.read().decode('utf-8'))