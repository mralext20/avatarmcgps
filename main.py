import math
currentX = eval(input("Please enter your current, or starting X coordinate: "))
currentZ = eval(input("Please enter your current, or starting Z coordinate: "))

#above gets current location, bellow finds out where you are trying to get to

targetX = eval(input("Please enter your target, or final X coordinate: "))
targetZ = eval(input("Please enter your target, or final Z coordinate: "))

#your bending type, used for finding if /capital is closer.

bendingInput = input("What type of bending do you use? valid choices are air, water, fire, earth: ")

bendingInput.upper()

if bending == "FIRE":
    capitalX = 3950
    capitalZ = 9760
elif bending == "AIR":
    capitalX = 10820
    capitalZ = 15010
elif bending == "WATER":
    capitalX = 13300
    capitalZ = 2030
elif bending == "EARTH":
    capitalX = 19780
    capitalZ = 5730
else:
    print("you didnt input a valid bending. continueing with no capital.")
    capitalX = 0
    capitalZ = 0

#well, now for the hardest part. the distance formula.
#current position to target.
currenttotarget = math.sqrt(math.pow(targetX-currentX,2)+math.pow(targetZ-currentZ,2))
currenttotarget = math.floor(currenttotarget)
print ("distance from starting point to the target: "+repr(currenttotarget))


#capital to target. now we check if capitalX is 0, and do not execute this portion.
if capitalX != 0:
     capitaltotarget = math.sqrt(math.pow(targetX-capitalX,2)+math.pow(targetZ-capitalZ,2))
     capitaltotarget = math.floor(capitaltotarget)
     print ("distance from your capital to the target: "+repr(capitaltotarget))
