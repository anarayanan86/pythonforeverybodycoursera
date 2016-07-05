import urllib
import xml.etree.ElementTree as ET

address = 'http://python-data.dr-chuck.net/comments_282902.xml'
a = urllib.urlopen(address)
b = a.read()
print b
c = ET.fromstring(b)
counts = c.findall('.//count')

d = []
for i in counts:
	d.append(i.text)
d = map(int, d)
print d
total = 0
for j in d:
	total += j
print "The sum is: ", total
