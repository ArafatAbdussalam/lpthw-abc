from sys import exit

def gold_room():
	print("This room is full of gold. How much do you take?")
	
	choice=input("> ")
	if "0" in choice or "1" in choice:
		how_much=int(choice)
	else:
		dead("Dear, learn to type a number.")
		
	if how_much < 50:
		print("Nice! You are no greedy. You win")
		exit(0)
	else:
		dead("You are too greedy, change!")
	
def bear_room():
	print("There is a bear here.")
	print("The bear has a bunch of honey")
	print("The fat bear is in front of another door")
	print("How are you going to move the bear?")
	bear_moved = False
	
	while True :
		choice=input("> ")
		
		if choice=="Take honey":
			dead("The bear looks at you, then slap your face off!")
		elif choice=="Taunt bear" and not bear_moved:
			print("The bear has moved from the door.")
			print("You can go through it now.")
			
			bear_moved= True
		elif choice=="Taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif choice == "Open door" and bear_moved:
			gold_room()
		else:
			print("I got no idea what that means")
	
def cthulu_room():
	print("Here, you see great evil Cthulu")
	print("He, It, whatever it is stares at you and go insane")
	print("Do you flee for your life or eat your head?")
	
	choice=input("> ")
	
	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("Well, that was tasty")
	else:
		cthulu_room()
	
def dead(why):
	print(why, "Good job!")
	exit(0)
	
def start():
	print("You are in a dark room")
	print("There is a door to your right and left.")
	print("Which one do you take?")
	
	choice=input("> ")
	
	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulu_room()
	else:
		dead("You stumble around the roim until you starve")
		
start()

