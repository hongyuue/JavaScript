the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1,'pennies',2,'dimes',3,'quarters']
#thid first kind of for-loop goes through a list
for number in the_count:
	print "This is count %d" % number
	
#same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit
	
#alse we can go through mixed lists too 
#notice we have use %r since we don't know what's in items
for i in change:
	print "I got %r" %i

# we can also bulid lists, first start with an empty one
elements = []
elements = range(0,6)
#then use the range function to do 0 to 5 count
# for i in range(0,6):
	# print "Adding %d to the list" % i
	# #append is a function that lists understand 
	# elements[i] = i
	
#now we can print them out too
for i in elements:
	print "Element was :%d" % i
	

