from house import House
from contract import Contract

class Rental(object):
    def __init__(self, residence, rental):
        self._residence = residence
        self._rental = rental

    def getResidence(self):
        return self._residence

    def setResidence(self, residence):
        self._residence = residence

    def getRental(self):
        return self._rental

    def setRental(self, rental):
        self._rental = rental

    def __str__(self):
        return ("Residence Details: %s\nRental Details:%s\n%s" % (self._residence, self._rental, "-"*15))

def main():
    house = House(1200, "Western Road", 2, True)
    contract = Contract("31-Dec-2016", 1200.00)

    rental = Rental(house, contract)
    print(rental)

if __name__ == "__main__":
    main()
