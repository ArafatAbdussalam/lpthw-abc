import sys 
script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
	line = language_file.readLine()
	
	if line:
		print_line(line, encoding, errors)
		return main(language_file, encoding, errors)
		
def print_line(line, encoding, errors):
	next_lang = Line.strip()
	raw_bytes = next_lang.encode(encoding, errors=errors)
	cooked_string = raw_bytes.decode(encoding, errors=errors)
	print(raw_bytes, "<===>", cooked_string)
	
languages = open("languages.txt", encoding="urf-8")

main(languages, input_encoding, error)

#UTF-8 means Universal-encoding Transformation Format -8 bits
#8 bits make a byte

#$ python3.6 utf-8 strict

# >>>0b1011010
#>>> ord('Z')
# >>> chr(90)