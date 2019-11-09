from property import Property

class Appartment(Property):

    def __init__(self, floorarea,  address, appartmentNo, hasBalcony):
        Property.__init__(self, floorarea, address)
        self._appartmentNo = appartmentNo
        self._hasBalcony = hasBalcony

    def getAppartmentNo(self):
        return self._appartmentNo

    def setAppartmentNo(self, appartmentNo):
        self._appartmentNo = appartmentNo

    def getBalcony(self):
        return self._hasBalcony

    def setBalcony(self, hasBalcony):
        self._hasBalcony = hasBalcony

    def getAddress(self):
        return ("Apartment %i, %s" % (self._appartmentNo, self._address))

    def __str__(self):
        hasBalconyStr = "Has No Balcony"
        if self._hasBalcony:
            hasBalconyStr = "Has Balcony"
        return ("%s, AppartmentNo: %i, %s" % (Property.__str__(self), self._appartmentNo, hasBalconyStr))

    address = property(getAddress, Property.setAddress)
    appartmentNo = property(getAppartmentNo, setAppartmentNo)
    balcony = property(getBalcony, setBalcony)

def main():
    appartment = Appartment(1200, "Western Road", 1, True)
    print(appartment)

    appartment.address = "Cork City"
    appartment.appartmentNo = 10
    print(appartment.address)

if __name__ == "__main__":
    main()
