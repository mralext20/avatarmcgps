import math
from mathUtil import MathUtil
from coordinate import Coordinate
from TownListHandler import TownListHandler

#TODO: Clean this up and make a function that takes a string and returns a Coordinate
currentLocationInput = input("Please enter your current location, in X,Z format (Example: 230,134): ")
currentLocationList = currentLocationInput.split(",", 1)
currentLocationCoordinate = Coordinate(currentLocationList[0], currentLocationList[1])
currentLocationCoordinate.printCoordinate()

targetInput = input("Please enter your target location, in X,Z format (Example: 230,134): ")
targetCoordinateList = targetInput.split(",", 1)
targetCoordinate = Coordinate(targetCoordinateList[0], targetCoordinateList[1])
targetCoordinate.printCoordinate()

#TODO: Move this to it's own class? Just have it return a Coordinate perhaps?
while (True):
	bendingInput = input("\nWhat type of bending do you use? Valid choices are air, water, fire, earth: ")
	bendingInput = bendingInput.upper()

	if bendingInput == "FIRE":
		capitalCoordinate = Coordinate(3950, 9760)
		break;
	elif bendingInput == "AIR":
		capitalCoordinate = Coordinate(10820, 15010)
		break;
	elif bendingInput == "WATER":
		capitalCoordinate = Coordinate(13300, 2030)
		break;
	elif bendingInput == "EARTH":
		capitalCoordinate = Coordinate(19780, 5730)
		break;
	else:
		print("\nYou didn't give a valid input. \n")

while (True):
    nationInput = input("What player nation are you a part of? (To see a list, type 'List'): ")
    nationInput = nationInput.upper()

    if nationInput == "LIST":
        TownListHandler.printNationList()
    elif nationInput == "NONE":
        break;
    else:
        if TownListHandler.hasNation(nationInput):
            break;
        else:
            print("\nI dont appear to have your nation yet... file an issue at github.com/mralext20/avatarmcgps\n\n\n in the mean time, just type none.")


targetDistance = MathUtil.getDistance(currentLocationCoordinate, targetCoordinate)

print ("Distance from starting point to the target: " + str(targetDistance))

#capital to target. now we check if capitalX is 0, and do not execute this portion.
if bendingInput != "NONE":
    capitalDistance = MathUtil.getDistance(targetCoordinate, capitalCoordinate)
    print ("Distance from your capital to the target: " + str(capitalDistance))

if nationInput != "NONE":
    townList = TownListHandler.getNationTownList(nationInput)

    for town in townList:
        townCord = TownListHandler.getTownCord(nationInput, town)
        townDistance = MathUtil.getDistance(targetCoordinate, townCord)

        print(str(townDistance) +" is the distance from " + town.upper() + " to your target")
