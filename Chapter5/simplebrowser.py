import urllib2
url = "http://nostarch.com"
#url = "http://google.com"
print "URL =", url
body = urllib2.urlopen(url)
print "Got it. Converting"
readable = body.read()
print readable