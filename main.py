import math
from mathUtil import MathUtil
from cordinate import Cordinate
from TownListHandler import TownListHandler

#TODO: Clean this up and make a function that takes a string and returns a Cordinate
currentLocationInput = input("Please enter your current location, in X,Z format (Example: 230,134): ")
currentLocationList = currentLocationInput.split(",", 1)
currentLocationCordinate = Cordinate(currentLocationList[0], currentLocationList[1])
currentLocationCordinate.printCordinate()

targetInput = input("Please enter your target location, in X,Z format (Example: 230,134): ")
targetCordinateList = targetInput.split(",", 1)
targetCordinate = Cordinate(targetCordinateList[0], targetCordinateList[1])
targetCordinate.printCordinate()

#TODO: Move this to it's own class? Just have it return a Cordinate perhaps?
while (True):
	bendingInput = input("\nWhat type of bending do you use? Valid choices are air, water, fire, earth, or none: ")
	bendingInput = bendingInput.upper()

	if bendingInput == "FIRE":
		capitalCordinate = Cordinate(3950, 9760)
		break;
	elif bendingInput == "AIR":
		capitalCordinate = Cordinate(10820, 15010)
		break;
	elif bendingInput == "WATER":
		capitalCordinate = Cordinate(13300, 2030)
		break;
	elif bendingInput == "EARTH":
		capitalCordinate = Cordinate(19780, 5730)
		break;
	elif bendingInput == "NONE":
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
    '''
    if playernation == "PANELEMENTA":
        nationtowns=[("hyperborea", 15280, 3765),("jiangshi", 18696, 8258),("frostfire", 13190, 916),("nenshoken", 5599, 10921),("golae", 13545, 13314),("Puraheadquarter", 14508, 8404),("SouthernRaders", 12981, 13449),("NaiSui", 9670, 5215),("Khorg Maldur", 4661, 10851),("Fuego del Mar", 12952, 584)]
        break;
    '''
    
targetDistance = MathUtil.getDistance(currentLocationCordinate, targetCordinate)

print ("Distance from starting point to the target: " + str(targetDistance))

#capital to target. now we check if capitalX is 0, and do not execute this portion.
if bendingInput != "NONE":
    capitalDistance = MathUtil.getDistance(targetCordinate, capitalCordinate)
    print ("Distance from your capital to the target: " + str(capitalDistance))

if nationInput != "NONE":
    townList = TownListHandler.getNationTownList(nationInput)
    
    for town in townList:
        townCord = TownListHandler.getTownCord(nationInput, town)
        townDistance = MathUtil.getDistance(currentLocationCordinate, townCord)
        
        print("Your current distance from " + town.upper() + " is : " + str(townDistance))
