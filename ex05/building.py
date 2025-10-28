import sys
import unicodedata as ud

def ft_len(obj):
    i = 0
    try:
        while True:
            obj[i]
            i += 1
    except IndexError:
        return i
	
def is_upper(ch):
    return ud.category(ch) in ("Lu", "Lt")

def is_lower(ch):
    return ud.category(ch) == "Ll"

def is_digit(ch):
    return ud.category(ch) == "Nd"

def is_punct(ch):
    return ud.category(ch).startswith("P")

def is_space(ch):
    cat = ud.category(ch)
    return cat.startswith("Z") or ch in " \t\r\v\b\f\n"

def	ft_lowchars(text):
	i = 0
	n = 0
	length = ft_len(text)
	while i < length:
		try:
			c = text[i]
		except IndexError:
			break
		if is_lower(text[i]):
			n = n + 1
		i = i + 1
	return n

def	ft_upchars(text):
	i = 0
	n = 0
	length = ft_len(text)
	while i < length:
		try:
			c = text[i]
		except IndexError:
			break
		if is_upper(text[i]):
			n = n + 1
		i = i + 1
	return n

def ft_punctchars(text):
	i = 0
	n = 0
	length = ft_len(text)
	punct = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
	while i < length:
		if is_punct(text[i]):
			n = n + 1
		i = i + 1
	return n

def	ft_spacechars(text):
	i = 0
	n = 0
	length = ft_len(text)
	while i < length:
		if is_space(text[i]):
			n = n + 1
		i = i + 1
	return n

def ft_digitchars(text):
	i = 0
	n = 0
	length = ft_len(text)
	while i < length:
		if is_digit(text[i]):
			n = n + 1
		i = i + 1
	return n

def	main(argv):
	text = None
	length = ft_len(argv)
	if length == 1:
		try:
			text = input("What is the text to count?\n")
		except (EOFError, KeyboardInterrupt):
			print("\nNo data provided to input function")
			return 1
	elif length > 2:
		print(f"AssertionError: Expected one argument to the program")
		return 1
	else:
		text = argv[1]
	print(f"The text contains {ft_len(text)} characters:")
	print(f"{ft_upchars(text)} upper letters")
	print(f'{ft_lowchars(text)} lower letters')
	print(f'{ft_punctchars(text)} punctuation marks')
	print(f'{ft_spacechars(text)} spaces')
	print(f'{ft_digitchars(text)} digits')
	return 0

if __name__ == "__main__":
	sys.exit(main(sys.argv))