# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
count = int(raw_input("Enter count: "))
position = int(raw_input("Enter position: "))

names = []

while count > 0 :
	print "Retrieving: {0}".format(url)
	page = urllib.urlopen(url)
	soup = BeautifulSoup(page)
	tag = soup('a')
	name = tag[position - 1].string
	names.append(name)
	url = tag[position - 1]['href']
	count -= 1
print names[-1]
