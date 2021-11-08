from sys import argv
script, first, second, third = argv

print("This script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# run this on the terminal by typing
#python 3.6 ex3.py first 2nd 3rd
# run more by typing 
#python3.6 ex3.py stuff thing
# notice what changes

#int(input())


from sys import argv
script, user_name = argv
prompt='> '

print(f"Hi {username}, I am the {script} script.")

print("I'd like to ask you a few questions")
print(f"Do you like me? {user_name}")
likes=input(prompt)

print(f"where do you live {user_name}?")
lives = input(prompt)

print("what kind of computer do you have?")
computer = input(prompt)

print(f""
	Alright, you said {likes} about liking me.
	You live in {lives}. Not sure where that is.
	And you have a {computer}. That is nice."")

#python ex3.py Arafat

from sys import argv

script, filename = argv

text=open(filename)

print(f"Here is your file: {filename}:")
print(text.read())


print("Type the filename again:")
file_again= input(">  ")

txt_again = open(file_again)
print(txt_again.read())

#make a file called ex3_sample.txt
#commands or functions or method

#sys is a package

#close, read, readLine, truncate-empties fike, write("stuff"), seek(0)

from sys import argv
script, file_name = argv

print(f"We are going to erase {filename}.")

print("If you don't want that hit CTRL-C (^C).")

print("If you do want that hit RETURN")

input=("?  ")

print("opening the file....")
target = open(filename, "w")

print("Truncating the file...Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("I'm going to write this to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it")
target.close()

#python3.6 ex3.py test.txt

#"w"- open this file in write mode

#read(r), append(a), modifiers(r+,w+)

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"copying from{from_file} to {to_file}.")

#we could do this on one line like this

in_file = open(from_file)
indata = in_file.read()
print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exist(to_file})")

print("hit RETURN to continue, CTRL-C to abort")
input()

out_file = open(to_file, "w")
out_file.write(indata)

print("All right, all done.")

out_file.close()
in_file.close()

#the exists function returns True if a file is found

# command line crash course

#cat concatenates file together

$# first make a sample file
$ echo "This is a test file." > test.txt

$ cat test.txt

This is a test file

# run your script on it

python3.6 ex3.py test.txt new_file.txt

