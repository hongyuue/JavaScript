from sys import exit
from random import randint

def death():
	quips = ["You died. You kinda suck at this.",
			"Nice job, you died ... jackass.",
			"Such a luser.",
			"I have a small puppy that's better at this."]
	print quips[randint(0,len(quips) - 1)]
	exit(1)
	
	
def central_corridor():
	print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
	print "Your entire crew. Your are the last surviving mamber and your last"
	print "mission is to get the neutron destruct bomb from the Weapons Armory"
	print "put is in the bridge, and blow the ship up after getting in an"
	print "escape pod."
	print "\n"
	print "You're running down the central corridor to the Weapons Armory when"
	print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
	print "flowing around his hate filled body. He's blocking the door to the"
	print "Armory and about to pull a weapon to blast you."
	
	action = raw_input(">")
	
	if action == "shoot!":
		print "Quict on the draw you yank out your blaster and fire it at the Gothon."
		print "His clown costume is flowing and moving around his body,which throws"
		print "off your aim. Your laser hits his costume but misses him entirely. This "
		print "completely ruins his brand new costume his mother bought him, which"
		print "makes him fly into an insane rage and blast you repeatedly in the face until"
		print "you are dead. Then he eats you."
		return 'death'
		
		
	elif action == "dodge!":
		print "Like a world class boxer you dodge, weave ,slip and slide right"
		print "as the Gothon's blaster cranks a laser past your head."
		print "In the middle of your artful dodge your foot slips and you"
		print "bang your head on the metal wall and pass out."
		print "You wake up shortly after only to die as the Gothon stomps one"
		print "your head and eats you."
		return 'death'
		
	elif action == "tell a joke":
		print "Luckly for you they made you learn Gothon insults in the academy"
		print "You tell the one Gothon joke you know:"
		print "Lbhe zbgure vf fb sng, jura fur vfgf nebhaq gurubhfr, fur fvgf nebhaq gur ubhfr."
		print "The Gothon stops, tries not to laugh,then busts out laghing and cat't move"
		print "While he's laughing you run up and shoot him square in head"
		print "putting him down,then jump through the Weapons Armorydoor."
		return "laser_weapon_armory"
		
	else:
		print "DOSE NOT COMPUTE!"
		print "central_corridor"
	
def laser_weapon_armory():
	print "You do a dive roll into the Warning Armory ,crouch and scan the room"
	print "for more Gothons that might be hding. It's dead quiet,too quiet"
	print "You stand up and run to the far side of the room and find the"
	print "neutorn bomb in its container. There's a keypad lock on the box"
	print "and you need the code to get the bomb out. If you get the code"
	print "wrong 10 times then the lock closes forever and you cat't"
	print "get the bomb . The code is 3 digits."
	code = "%d%d%d" % (randint(1,9),randint(1,9),randint(1,9))
	guess = raw_input("[keypad]")
	guesses = 0
	
	while guess != code and guesses < 10:
		print "BZZZZEDDD!\a"
		guesses += 1
		guess = raw_input("[keypad]")
		
	if guess == code:
		print "The container clicks open and the seal breaks,letting gas out"
		print "You grab the neutron bomb and run as fast as you can to the "
		print "bridge where you must place it in the right spot."
		return 'the_bridge'
		
	else:
		print "the lock buzzes one last time and then you hear a sickening"
		print "melting sound as the mechanism is fused together"
		print "You dicide to sit there,and finally the Gothons blow up the"
		print "ship from their ship and you die."
		return 'death'
		
		
def the_bridge():
	print "You burst on to the Brudge with the neutron destruct bomb"
	print "under your arm and surprise 5 Gothons who are trying to"
	print "take control of the ship. Each of them has aneven uglier"
	print "weapon out yet, as they see the active bomb under your:"
	print "arm and don't want to set is off"
	
	action = raw_input(">")
	if action == "throw the bomb":
	print "In a panic you throw the bomb at the group of Gothons"
	print "and make a leap for the door. Right as you drop is a"
	print "Gothon shoots you right in the back killing you"
	print "As you die you see another Gothon frantically try to disarm"
	print "the bomb . You die knowing they will probably blow up when"
	print "it goes off."
	return 'death'
	
	elif action == "slowly palce the bomb":
		print "You point your blaster at the bomb under your arm"
		print "and the Gothons put their hands up and start to sweat."
		print 
		
