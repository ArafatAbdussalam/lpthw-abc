"""
mystuff = {"apple": "I am apples!"}
print(mystuff["apple"])

def apple():
	print("I am aples")
	
	tangerine= "Living reflection of a dream"

mystuff.tangerine

mystuff is a module 

import mystuff
mystuff.apple()


class mystuff(object):
  	
  	def __init__(self):	
  		" set tangerine instance variable "
  		self.tangerine="And now a thousand years between"
  		
  	def apple(self):
  		print("I am classy apples!")

"""

class song(object):
	
	def __init__ (self, lyrics):
		self.lyrics=lyrics
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print(line)
			
happy_bday = song(["Happy birthday to you",
"Hehe! I don't want to get sued!"
"So I'll stop right there"])

bulls_on_parade = song(["They rally around the family",
"with pocket full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

# new script

import random
from urlib.request import urlopen
import sys

WORD_URL = "https://learncodethehardway.org/word.txt"
WORDS = [ ]

PHRASES = {
"class X(Y): "
"Make a class names X that is-a Y.",
"class X (object):\n\t def __init__(self, J)":
	"class X has-a __init__ that takes self and J parameters.",
"class X (object):\n\t def F(self, J)":
	"class X has-a F function, call it with its params self and J.",
	"a.b(c)' ":
		"from a get the b function, call it with params self , c",
	"a.b = 'c' ":
		"from a get the attribute b and set it to c"
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "English":
	PHRASE_FIRST = True
else:
	PHRASE_FIRST = False
	
	# load up the words from the website
for word in urlopen(WORD_URL).readLines():
	WORDS.append(str(word.strip(), encoding ="utf-8"))
	
def convert(snippet, phrase):
	class_names =[w.capitalize() for w in 
	random.sample(WORDS, snippet.count("abc")) ]
	
	other_names=random.sample(WORDS, snippet.count("def"))
	result = []
	param_names= []
	
	for i in range(0, snippet.count"xyz"):
		param_count = random.radinit(1,3)
		param_names.apoend(', '.join(random.sample[words, param_count]))
	
	for sentence in snippet, phrase:
		result = sentence [ : ]
		
		# fake class names
		
		for word in class_names:
			result = result.replace("xyz", word, 1)
			results.append(result)
			
#keep trying until they hit CTRL-D

try:
		while True:
			snippets = list[PHRASES.keys()]
		
		
