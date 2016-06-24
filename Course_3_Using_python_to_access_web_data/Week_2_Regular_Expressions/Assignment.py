import re
a = open('regex_sum_282900.txt')
b = a.read()
c = re.findall("[0-9]+", b)
d = [int(i) for i in c]
sum = 0
for j in d:
	sum += j
print sum
