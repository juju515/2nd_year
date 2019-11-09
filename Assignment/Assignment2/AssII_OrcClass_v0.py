from Assignment.Assignment2.AssII_CharacterClass_v0 import Character
import shelve

class Orcs(Character):
    """
    Creating the class Orcs
    Orcs have the following attributes:
        - name       -->   user input
        - weapon     -->   True or False (if no input is given: False)
        - skill      -->   int: 1 to 10
        - strength   -->   int: 1 to 10
    """
    def __init__(self, name, skill, strength, weapon = False):
        Character.__init__(self, name, skill, weapon)
        self.strength = strength

    # string representation:
    def __str__(self):
        """
        String function for printing the information on the Orc instance
        """
        return ("\r Name: %s \n Weapon: %s \n Skill: %.1f \n Strength: %.1f" %
                (self.name, self.weapon, self.skill, self._strength))              # prints the class instance

    # function for saving instances to the shelve:
    def saveOrc(self):
        with shelve.open("orc_"+self.name) as shelf:                            # opening/closing the shelve with "with"
            shelf["nameKey"] = self.name                                        # saving the instance attributes
            shelf["weaponKey"] = self.weapon                                    # under [nameKey], [weaponKey],
            shelf["strengthKey"] = self._strength                                # [strengthKey] and [skillKey]
            shelf["skillKey"] = self.skill

    @property
    def strength(self):
        """
        getter for _weapon attribute
        """
        return self._strength

    @strength.setter
    def strength(self, strength):
        """
        Setter for _strength attribute
        """
        if strength < 0:                                                         # making sure strength is > 0 and < 10
            return False
        if strength > 10:
            return False
        else:
            self._strength = strength

# testing
def main():
    pass

if __name__ == "__main__":
    main()