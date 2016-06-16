import configparser
from cordinate import Cordinate

class TownListHandler:
    def getConifg():
        fileName = 'TownList.ini'
        config =  configparser.ConfigParser()
        config.read(fileName)
        
        return config
    
    def printNationList():
        config = TownListHandler.getConifg()
        nationList = config.sections()
        
        print("\n   Nations    ")
        print ("---------------")
        for nation in nationList:
            print(" * " + nation)

    def printTownList(nationName):
        config = TownListHandler.getConifg()
        townList = config.options(nationName)
        
        print("\n   " + nationName + "    ")
        print ("---------------")
        for town in townList:
            print(" * " + town)
            
    def hasNation(nationName):
        return TownListHandler.getConifg().has_section(nationName)
    
    def hasTown(nationName, townName):
        return TownListHandler.getConifg.has_option(nationName, townName)
    
    def getTownCord(nationName, townName):
        config = TownListHandler.getConifg()
        cordString = config.get(nationName, townName)
        cordStringValues = cordString.split(",", 1)
        townCord = Cordinate(int(cordStringValues[0]), int(cordStringValues[1]))
        
        return townCord
    
    def getNationTownList(nationName):
        config = TownListHandler.getConifg()
        townList = config.options(nationName)
        
        return townList

#TODO: These functions?
'''
    def getClosestTowns(cordCurrent):
    
    def getClosestNationTowns(cordCurrent, nationName):
'''