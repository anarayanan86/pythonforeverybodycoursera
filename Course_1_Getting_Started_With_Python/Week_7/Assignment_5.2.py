#5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter the numbers from the book for problem 5.1 and Match the desired output as shown.

largest = None
smallest = None
c = []
a = True
while a == True:
    num = raw_input("Enter a number: ")
    if num == "done":
		largest = max(c)
		smallest = min(c)       
		break
    try:
    	b = int(num)
    	c.append(b)
    except:
        print("Invalid input")

print "Maximum is", largest
print "Minimum is", smallest
