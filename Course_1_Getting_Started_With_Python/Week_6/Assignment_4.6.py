def computepay(h,r):
	h = raw_input("Enter Hours:")
	hrs = float(h)
	r = raw_input("Enter rate:")
	rate = float(r)
	total = 0
	if hrs <= 40:
		total = hrs * rate
	else:
		overtime = hrs - 40
		total = 40 * rate + (overtime * (rate * 1.5))
	return total
    
    
p = computepay(45,10.5)
print p
