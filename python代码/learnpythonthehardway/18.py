# this one is like your scripts with argv

def print_two(*argv):
	arg1, arg2 = argv
	print "arg1:%r ,arg2:%r" %(arg1,arg2)
	
	
# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1,arg2):
	print "arg1: %r ,arg2 :%r" %(arg1,arg2)
	
	
# this just tokes one argument
def print_one(arg1):
	print "arg1: %r " % arg1

	
# this one takes no arguments
def print_none():
	print "I got nothin',"
	
print_two("zed","shaw")
print_two_again("Zed","shaw")
print_one("Frist!")
print_none()
