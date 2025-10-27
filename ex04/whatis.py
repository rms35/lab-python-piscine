#!/usr/bin/env python3
import sys

def main(argv):
	if len(argv) != 2:
		print("Error: Expected one argument to the program")
		return 1
	try:
		n = int(argv[1])
	except ValueError:
		print("Error: arg is not an integer")
		return 1
	if ((int(argv[1])) % 2 == 0):
		return print("I'm Even")
	print("I'm Odd")

if __name__ == "__main__":
	sys.exit(main(sys.argv))