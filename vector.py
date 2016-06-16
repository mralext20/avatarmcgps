class Vector:
    def __init__(self, xDirection, zDirection):
        self.xDirection = xDirection
        self.zDirection = zDirection
    
    def getLength(self):
        length = math.sqrt(math.pow(self.xDirection, 2) + math.pow(self.zDirection, 2))
        return length
    
    def printVector(self):
        print ("Vector: %s, %s") % (self.xDirection, self.zDirection)
        
    def getUnitVector(self):
        length = getLength()
        
        shortXDirection = round(self.xDirection/length, 2)
        shortYDirection = round(self.yDirection/length, 2)
        
        unitVector = Vector(shortXDirection, shortYDirection)
        
        return unitVector