def print_two(*args):
	arg1, arg2 = args
	print(f"arg1: {arg1}, arg2: {arg2}")
	
def print_two_again(arg1, arg2):
	print(f"arg1: {arg1}, arg2: {arg2}")
	
def print_one (arg1):
	print(f"arg1: {arg1}")
	
def print_none():
	print("I got nothing")
	
print_two("Arafat", "Abdussalam")
print_two_again("Arafat", "Asake")
print_one("food")
print_none()

# your function should have a short name that explains what it does

def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print(f"You have {cheese_count} cheese")
	print(f"You have {boxes_of_crackers} boxes of crackers")
	
print(f"We can just give the function numbers directly")
cheese_and_crackers(20, 30)

print("Or we can use variables from our scripts.")
amount_of_cheese = 10
amount_of_crackers += 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do Maths inside:")
cheese_and_crackers(10 + 20 / 4, 20.0 + 6)


#new

from sys import argv

script, input_file = argv

def print_all(f):
	print(f.read())

def rewind(f):
# move to the start of the file. it deals wirh byte, not line
	f.seek(0)
	
def print_a_line(line_count, f):

current_file = open(input_file)

print("Alright, let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_line)

current_line = current_line + 1
print_a_line(current_line, current_line)


	#new
	
def add(a,b):
	print(f"ADDING {a} + {b}")
	return a + b
	
def subtract(a, b):
	print(f"SUBTRACTING {a} - {b}")
	return a - b
	
def multiply(a, b):
	print(f"MULTIPLYING {a} * {b}")
	return a * b
	
def divide(a, b):
	print(f"DIVIDING {a} / {b}")
	return a / b
	
print("Let's do some maths with just functions!")

age=add(12,9)
height=subtract(90,8)
weight=multiply(100,2)
iq=divide(280,2)


print(f"Age: {age}, Weight: {weight}, Height: {height}, IQ= {iq}")

print("Here is a puzzle")

what=add(age, subtract(height, multiply(weight, divide(iq,2))))

print("That becomes: ", what, "Can you do it by hand?")

#float(input())


	