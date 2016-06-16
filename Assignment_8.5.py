#8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
#Hint: make sure not to include the lines that start with 'From:'.
#You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt

#fname = raw_input("Enter file name: ")
#if len(fname) < 1 : fname = "mbox-short.txt"
fname = open("mbox-short.txt")
a = fname.read()
#print a
b = a.split("\n")
#print b
count = 0
for i in b:
    if i.startswith("From "):
        c = i.split()
        print c[1]
#        print i[1]
#        b = i.split(":")
#        print b[1]
        count = count + 1

print "There were", count, "lines in the file with From as the first word"
