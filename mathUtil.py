import math
from cordinate import Cordinate
from vector import Vector
 
class MathUtil:

    def getDistance(pointA, pointB):
        xValue = pointB.xCord - pointA.xCord
        zValue = pointB.zCord - pointA.zCord
        
        distance = round(math.sqrt(math.pow(xValue, 2) + math.pow(zValue, 2)), 2)
        
        return distance
    
    def getVector(pointA, pointB):
        xValue = pointB.xCord - pointA.xCord
        zValue = pointB.zCord - pointA.zCord
        
        return Vector(xValue, zValue)