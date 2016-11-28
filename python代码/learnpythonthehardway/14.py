from  sys import argv


script, user_name , say_hello = argv 

prompt = ': '

#print "%s" % say_hello

print "%s %s, I'm the %s script." % (say_hello,user_name,script)

print "I'd like to ask you a few questions."

print "Do you liked me %s" % user_name

likes = raw_input(prompt)

print "Wherer do you live %s ?" % user_name

lives = raw_input(prompt)

print "What kind of computer do you have?" 
computer = raw_input(prompt)

print '''
Alright, so you said %s about liking me.
You live in %r , Not sure where that is,
And you have a %r computer. Nice.
''' % (likes, lives, computer)


