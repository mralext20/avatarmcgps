import math
current = eval(input("Please enter your current location, in X, Z format: "))

#above gets current location, bellow finds out where you are trying to get to

target = eval(input("Please enter your target, in X, Z format: "))

#your bending type, used for finding if /capital is closer.

while (True):
	bending = input("What type of bending do you use? Valid choices are air, water, fire, earth, or none: ")
	bending = bending.upper()

	if bending == "FIRE":
		capital = (3950, 9760)
		break;
	elif bending == "AIR":
		capital = (10820, 15010)
		break;
	elif bending == "WATER":
		capital = (13300, 2030)
		break;
	elif bending == "EARTH":
		capital = (19780, 5730)
		break;
	elif bending == "NONE":
		capital = 0
		break;
	else:
		print("\nYou didn't give a valid input. \n")


#well, now for the hardest part. the distance formula.
#current position to target.
targetDistance = ((target[0] - current[0]),(target[1] - current[1]))
capitalDistance = ((target[0] - capital[0]), (target[1] - capital[1]))

targetDistance = math.sqrt(math.pow(targetDistance[0],2)+math.pow(targetDistance[1],2))
targetDistance = math.floor(targetDistance)
print ("Distance from starting point to the target: " + repr(targetDistance))


#capital to target. now we check if capitalX is 0, and do not execute this portion.
if capital != 0:
    capitalDistance = math.sqrt(math.pow(capitalDistance[0],2)+math.pow(capitalDistance[1],2))
    capitalDistance = math.floor(capitalDistance)
    print ("Distance from your capital to the target: " + repr(capitalDistance))
