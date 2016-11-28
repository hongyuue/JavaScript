def add(a,b):
	print "ADDING %d + %d" %(a,b)
	return a + b
	
def subtract(a,b):
	print "SUBTRACTING %d - %d" %(a,b)
	return a - b

def multiply(a,b):
	print "MULTIPYING %d * %d" %(a,b)
	return a * b 
	
def divide(a,b):
	print "DIVIDING %d / %d" % (a,b)
	return a / b 

print "Let't do some math with just functions!"


age = add(30,5)

height = subtract(78,4)

weight = multiply(90,2)

iq = divide(100,2)

print "Age: %d\nHeight : %d\nWeight : %d\nIQ : %d\n" %(age,height,
weight,iq)

#A puzzle for the extra credit,type in in anyway
print "Here is a puzzle"

#what = add(age,subtract(height,multiply(weight,divide(iq,2))))
a = divide(iq,2)
b = multiply(weight,a)
c = subtract(height,b)
d = add(age,c)
what = d
print "That becomes:",what ,"Can you do it by hand?"