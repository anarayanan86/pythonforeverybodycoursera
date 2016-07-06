import urllib
import json

url = 'http://python-data.dr-chuck.net/comments_282906.json'
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved', len(data), 'characters'
#print data

info = json.loads(data)
a = info["comments"]
#print a
total = 0
for item in a:
	total += item['count']
print "The total of the counts is: ", total
