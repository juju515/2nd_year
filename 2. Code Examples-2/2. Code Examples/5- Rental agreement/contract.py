class Contract(object):

    def __init__(self, expires, rent):
        self._expires = expires
        self._rent = rent

    def getRent(self):
        return self._rent

    def setRent(self, rent):
        self._rent = rent

    def getExpires(self):
        return self._expires

    def setExpires(self, expires):
        self._expires = expires

    def __str__(self):
        return ("Expires:%s Rent:%.2f" % (self._expires, self._rent))

    rent = property(getRent, setRent)
    expires = property(getExpires, setExpires)

def main():

    contract = Contract("31-Dec-2016", 1200.00)
    print(contract)

    contract.expires = "31-Jan-2017"
    contract.rent = 1500.00

    print(contract)
    print("%s %.2f" % (contract.expires, contract.rent))

if __name__ == "__main__":
    main()
