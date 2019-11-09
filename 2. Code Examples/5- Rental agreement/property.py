class Property(object):

    def __init__(self, floorarea,  address):
        self._floorarea = floorarea
        self._address = address

    def getFloorArea(self):
        return self._floorarea

    def setFloorArea(self, floorarea):
        self._floorarea = floorarea

    def getAddress(self):
        return self._address

    def setAddress(self, address):
        self._address = address

    def __str__(self):
        return ("Floorarea: %i  Address: %s" % (self._floorarea, self._address))

    floorarea = property(getFloorArea, setFloorArea)
    address = property(getAddress, setAddress)

def main():
    prop = Property(1200, "Western Gateway Building")
    print(prop)

    prop.floorarea = 1300
    print(prop)

if __name__ == "__main__":
    main()
