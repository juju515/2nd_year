class Square(object):
    """Class to represent a square shape

    Class to represent a square shape and provide a description of its
    length of side, perimeter and area.

    Attributes:
        _length_of_side: length of a side of the square (protected)
        _area: area of the square (protected)
        _perimeter: total length of the perimeter (protected)
    """
    def __init__(self, length_of_side):
        """Constructor for square

        Inits Square object by setting _length_of_side and calculating area
        perimeters

        Args:
            length_of_side: a numeric value representing the squares side length
        """
        if length_of_side is None or length_of_side < 0:
            #TODO - add proper error handling
            print("Length of side is invalid")

        self._length_of_side = length_of_side
        self._area = self._length_of_side ** 2
        self._perimeter = self._length_of_side * 4

    @property
    def length_of_side(self):
        """Getter for the _length_of_side attribute

           Returns:
               An int representing the length of a square's side
        """
        return self._length_of_side

    @length_of_side.setter
    def length_of_side(self, length_of_side):
        """Setter for the _length_of_side attribute.

            Sets the attribute and recalculates area and perimeter

            Args:
                length_of_side: length of side for square
        """
        if length_of_side is None or length_of_side < 0:
            #TODO - add proper error handling
            print("Length of side is invalid")

        self._length_of_side = length_of_side
        self._area = self._length_of_side ** 2
        self._perimeter = self._length_of_side * 4

    @property
    def area(self):
        """Setter for the _length_of_side attribute.

            Sets the attribute and recalculates area and perimeter

            Args:
                length_of_side: length of side for square
        """
        return self._area

    @property
    def perimeter(self):
        """Getter for the _perimeter attribute

            Returns:
                int representing the length of the square's perimeter
        """
        return self._perimeter

    def __str__(self):
        """String method to generate a representation of the square

           Returns:
               string represention of the instance
        """
        descriptive_str = ("Side Length: %i - Area: %i - Perimeter: %i" % (
            self._length_of_side, self._area, self._perimeter))

        return descriptive_str

def main():
    """Main method that contains our test block
    """
    #We will test the instance by creating an instance, accessing values
    #and resetting length of side and inspecting effect.

    #Test initialisation of the square, confirm by reviewing its descriptive
    #string.
    square1 = Square(4)
    print(square1)

    #Update the length of the side of the square.
    square1.length_of_side = 5
    print(square1)

    #Values should correspond to the output above.
    print("Length of side: %i" % (square1.length_of_side))
    print("Length of perimeter: %i" % (square1.perimeter))
    print("Area of square: %i" % (square1.area))


if __name__ == "__main__":
    """Execution mode check to bypass tests for imports and run for direct
    execution.
    """
    main()
