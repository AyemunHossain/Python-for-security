import sys

try:
	print(f"You wrote in terminal: {sys.argv[1]}, {sys.argv[2]}")
except:
	print("You don't give input in terminal")