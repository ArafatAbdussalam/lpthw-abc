things=['a', 'b', 'c', 'd']
print(things[-4])

stuff={"name": "Arafat", "age": 108, "height": "6ft"}
print(stuff)

stuff['city']="SF"

print(stuff)

del stuff["name"]
#del stuff[0]

print(stuff)
print(stuff.items())

for stuff, assign in list(stuff.items()):
	print(f"{stuff} is assigned {assign}")
	
""" A list is an ordered list of items. A dict matches keys:values. Read more on dict dicumentation."""

