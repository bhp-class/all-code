import urllib2 as u2
url = "http://www.nostarch.com"
#url = "http://www.blackhatpython.com"
print "url = ",url
headers = {}
headers['User-Agent'] = "Googlebot"
request = u2.Request(url=url,headers=headers)
response = u2.urlopen(request)
print response.read()
response.close()

request2 = u2.Request(url,None,headers)