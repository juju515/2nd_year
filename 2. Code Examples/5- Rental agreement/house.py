from property import Property

class House(Property):

    def __init__(self, floorarea,  address, numfloors, hasgarage):
        Property.__init__(self, floorarea,  address)
        self._numfloors = numfloors
        self._hasgarage = hasgarage

    def getNumFloors(self):
        return self._numfloors

    def setNumFloors(self, numfloors):
        self._numfloors = numfloors

    def getHasGarage(self):
        return self._hasgarage

    def setHasGarage(self, hasgarage):
        self._hasgarage = hasgarage

    def __str__(self):
        hasGarageStr = "No Garage"
        if self._hasgarage:
            hasGarageStr = "Has Garage"
        return ("%s, %i bedrooms, %s" % (Property.__str__(self), self._numfloors, hasGarageStr))

def main():
    house = House(1200, "Western Road", 2, True)
    print(house)

if __name__ == "__main__":
    main()
