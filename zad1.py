import random

def termination():
	line = input("Do you want to exit? y/n ")
	if line == "y":
		return True
	return False	

while True:
	try:
		a = int( input("Please specify the lower boundary: ") )
	except ValueError:
		print("Wrong value of lower boundary.  Try again...")
		if termination():
			break	

	try:
		b = int( input("Please specify the upper boundary: ") )
	except ValueError:
		print("Wrong value of upper boundary.  Try again...")	
		if termination():
			break
		continue	


	if a<=b:
		c = random.randint(a, b)
		print(c)
	else:
		print("Value of lower boundary exceeds the vaule of upper boundary.  Try again...")

	if termination():
		break	

	
