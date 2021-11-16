def break_words(stuff):
	""" this function will break up the words for us """
	words=stuff.split(' ')
	return words
	
def sort_words(words):
	"""sort the words"""
	return sorted(words)
	
def print_first_word(words):
	"""prints the first word after poppingvit off """
	word=words.pop(0)
	print(word)
	
def print_last_word(words):
	""" prints the last word after popping it off"""
	word=words.pop(-1)
	print(word)
	
def sort_sentence(sentence):
	"""takes in a full sentence and return the sorted words."""
	words= break_words(sentence)
	return sort_words(words)
	
def print_first_and_last(sentence):
	""" prints the first and last word of the sentence"""
	words=break_words(sentence)
	print_first_word(sentence)
	print_last_word(words)
	
def print_first_and_last_sorted(sentence):
	"""sorts the words then print in the first and last one. """
	words=sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)
	
"""from ex7 import *
import ex7
sentence="All good things come to those who wait"
words=ex7.break_words(sentence)
words
sorted_words= ex7.sort_words(words)
sorted_words
ex7.print_first_word(words)
ex7.print_last_word(words)
words
ex7.print_first_word(sorted_words)
ex7.print_last_word(sorted_words)
sorted_words
sorted_words=ex7.sort_sentence(sentence)
sorted_words
ex7.print_first_and_last(sentence)
ex7.print_first_and_last_sorted(sentence)
this is a documentation document
type help(ex7.break_words)
"""

# save the script in a local directory.
# import ex7

"""
This code is broken, I need to fix it.
 
I will try to fix it on Github. This way, I learn how to use Github better

people = 20
cars = 40
trucks = 15

if cars > people and trucks > people :
	"" ret
	urns True and false ""
	print("We should take the cars")
elif cars < people:
	print("We should not take the cars")
else:
	print("We can't decide")
#x = range(1, 10)

#print("You enter a dark room with two #doors. 
#Do you go through door #1 or door #2?\""
)

door=input(">>> ")

if door == "1":
	print("There's a giant bear here eating a cheese cake.")
	print("What do you do?")
	print("1. Take the cake")
	print("2. Scream at the bear")
	
	bear=input(">>>  ")
	
	if bear =="1":
		print("The bear eats your face off. Good job!")
	elif bear=="2":
		print("The bear eats your leg off. Good job!")
	else:
			print(f"Well, doing {bear} is probably better.")
			print("Bear runs away")

	elif bear=="2":
		print("You stare into the endless abyss at Chulthu's retina")
		print("1. Blueberries!")
		print("2. Yellow jacket clover")
		print("3. Understanding revolving yelling melodies")
	
		insanity=input(">>  ")
		if insanity =="1" or insanity =="2":
			print("Your body survives powered by a mind of jello")
			print("Good job!")
		else:
			print("The insanity rots your eyes into a pool of muck.")
		print("Good job!")
else:
		print("You stumble around and fall on a knife and die.")
		print("Good job!")
"""

