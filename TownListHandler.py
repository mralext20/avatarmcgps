import configparser
from coordinate import Coordinate

class TownListHandler:
    def getConfig():
        fileName = 'TownList.ini'
        config =  configparser.ConfigParser()
        config.read(fileName)

        return config

    def printNationList():
        config = TownListHandler.getConfig()
        nationList = config.sections()

        print("\n   Nations    ")
        print ("---------------")
        for nation in nationList:
            print(" * " + nation)

    def printTownList(nationName):
        config = TownListHandler.getConfig()
        townList = config.options(nationName)

        print("\n   " + nationName + "    ")
        print ("---------------")
        for town in townList:
            print(" * " + town)

    def hasNation(nationName):
        return TownListHandler.getConfig().has_section(nationName)

    def hasTown(nationName, townName):
        return TownListHandler.getConfig.has_option(nationName, townName)

    def getTownCord(nationName, townName):
        config = TownListHandler.getConfig()
        cordString = config.get(nationName, townName)
        cordStringValues = cordString.split(",", 1)
        townCord = Coordinate(int(cordStringValues[0]), int(cordStringValues[1]))

        return townCord

    def getNationTownList(nationName):
        config = TownListHandler.getConfig()
        townList = config.options(nationName)

        return townList

#TODO: These functions?
'''
    def getClosestTowns(cordCurrent):

    def getClosestNationTowns(cordCurrent, nationName):
'''
