print("Let's practise everything.")
print('You\'d need to know \'bout with escapes  \\ that do:')
print('\n newlines and \t tabs')

poem ="""
\t the lovely world
with logic so firmly planted
cannot discern \n the need of love
nor comprehend passion from intuition
and requires an explanation
\n\t\t when there is none
"""

print("*" * 10)
print(poem)
print("*" * 10)

five = 20 - 2 + 3 + 6
print(f"This should be five: {five}")

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates
	
start_point = 10000 
beans, jars, crates = secret_formula(start_point)

# beans, jars and crates are argument variables called with secret_formula functions
# the variables are temporary and can be changed

print("With a starting point of: {}.".format(start_point))
print(f"We have {beans} beans, {jars} jars and {crates} crates")

# read the code backward

start_point = start_point / 10
print("We can also do that this way:")
formula = secret_formula(start_point)

# * means 
print("We'd have {} beans, {} jars and {} crates".format(*formula))


#new 

