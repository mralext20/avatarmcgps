import math
currentX = eval(input("Please enter your current, or starting X coordinate: "))
currentZ = eval(input("Please enter your current, or starting Z coordinate: "))

#above gets current location, bellow finds out where you are trying to get to

targetX = eval(input("Please enter your target, or final X coordinate: "))
targetZ = eval(input("Please enter your target, or final Z coordinate: "))

#your bending type, used for finding if /capital is closer.

while (true):
	bendingInput = input("What type of bending do you use? Valid choices are air, water, fire, earth, or none: ")
	bendingInput.upper()

	if bending == "FIRE":
		capitalX = 3950
		capitalZ = 9760
		break;
	elif bending == "AIR":
		capitalX = 10820
		capitalZ = 15010
		break;
	elif bending == "WATER":
		capitalX = 13300
		capitalZ = 2030
		break;
	elif bending == "EARTH":
		capitalX = 19780
		capitalZ = 5730
		break;
	elif bending == "NONE":
		capitalX = 0
		capitalZ = 0
		break;
	else:
		print("\nYou didn't give a valid input. \n")


#well, now for the hardest part. the distance formula.
#current position to target.
targetXDistance = (targetX - currentX)
targetZDistance = (targetZ - currentZ)
capitalXDistance = (targetX - capitalX)
capitalZDistance = (targetZ - capitalZ)

targetDistance = math.sqrt(math.pow(targetXDistance,2)+math.pow(targetZDistance,2))
targetDistance = math.floor(targetDistance)
print ("Distance from starting point to the target: " + repr(targetDistance))


#capital to target. now we check if capitalX is 0, and do not execute this portion.
if capitalX != 0:
    capitalDistance = math.sqrt(math.pow(capitalXDistance,2)+math.pow(capitalZDistance,2))
    capitaltotarget = math.floor(capitalDistance)
    print ("Distance from your capital to the target: " + repr(capitalDistance))
