from Assignment.Assignment2.AssII_CharacterClass_v0 import Character

class Humans(Character):
    """
    Creating the class Humans
    Humans have the following attributes:
        - name       -->   user input
        - weapon     -->   always True
        - skill      -->   int: 1 to 10
        - kingdom    -->   user input string
    """
    def __init__(self, name, skill, kingdom, weapon = True):
        Character.__init__(self, name, skill, weapon)
        self._kingdom = kingdom

    # getters
    @property
    def kingdom(self):
        """
        Getter for kingdom
        """
        return self._kingdom

    # setters:
    @kingdom.setter
    def kingdom(self, kingdom):
        """
        Setter for _name attribute
        """
        self._kingdom = kingdom

    # TODO - check if this actually works
    @weapon.setter
    def weapon(self, weapon):
        """
        Setter for _weapon attribute
        """
        if weapon is False:
            weapon is True
        else:
            self._weapon = weapon

# testing
def main():
    pass

if __name__ == "__main__":
    main()