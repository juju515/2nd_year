"""
CS2513 -  Intermediate Programming
_______________________________________

Assignment 1 - OOP
Part 1.a : Create a class
(W05-W06) - 10 marks
_______________________________________

Name:           Ozzak Jure Matic
Student num:    118743625

"""

import shelve


class Orcs:
    """
    Creating the class Orcs
    Orcs have the following attributes:
        - name       -->   user input
        - weapon     -->   True or False (if no input is given: False)
        - skill      -->   random: 1 to 10
        - strength   -->   random: 1 to 10
    """

    # constructor:
    def __init__(self, name, skill, strength, weapon=False):
        """
        constructor for class Orcs
        """
        self._name = name
        self._weapon = weapon
        self._skill = skill
        self._strength = strength

    # string representation:
    def __str__(self):
        """
        String function for printing the information on the Orc instance
        """
        return ("\r Name: %s \n Weapon: %s \n Skill: %.1f \n Strength: %.1f" %
                (self.name, self.weapon, self.skill, self.strength))              # prints the class instance

    # orcs greater than function (overloading with ">")
    def __gt__(self, other):
        draw = "It's a draw!"
        if self.weapon is False and other.weapon is False:                        # if both orks have NO weapon
            return self.strength > other.strength                                 # check the strength stats
        elif self.weapon is True and other.weapon is True:                        # if both orks have weapons
            return self.skill > other.skill                                       # check the skill stats
        elif self.weapon is True and other.weapon is False:                       # if only "self" ork has a weapon
            return True
        elif self.weapon is False and other.weapon is True:                       # is only "other" ork has a weapon
            return False
        else:
            return print(draw)                                                    # if it's a draw

    # orc attack function:
    def attack(self, opponent):
        if self > opponent:                                                       # if __gt__ returns True
            self.skill *= 1.05                                                    # increase the self.skill by 5%
            print(self.name, "won the fight and was rewarded +5% skill")          # and print "self" won
        else:                                                                     # if __gt__ returns False
            opponent.skill *= 1.05                                                # increase the other.skill by 5%
            print(opponent.name, "won the fight and was rewarded +5% skill")      # and print "other" won

    # function for saving instances to the shelve:
    def saveOrc(self):
        with shelve.open("orc_"+self.name) as shelf:                            # opening/closing the shelve with "with"
            shelf["nameKey"] = self.name                                        # saving the instance attributes
            shelf["weaponKey"] = self.weapon                                    # under [nameKey], [weaponKey],
            shelf["strengthKey"] = self.strength                                # [strengthKey] and [skillKey]
            shelf["skillKey"] = self.skill

    # getters:
    @property
    def name(self):
        """
        Getter for _name attributimport random
e
        """
        return self._name

    @property
    def weapon(self):
        """
        getter for _weapon attribute
        """
        return self._weapon

    @property
    def skill(self):
        """
        getter for _weapon attribute
        """
        return self._skill

    @property
    def strength(self):
        """
        getter for _weapon attribute
        """
        return self._strength

    # setters:
    @name.setter
    def name(self, name):
        """
        Setter for _name attribute
        """
        self._name = name

    @weapon.setter
    def weapon(self, weapon):
        """
        Setter for _weapon attribute
        """
        self._weapon = weapon

    @skill.setter
    def skill(self, skill):
        """
        Setter for _skill attribute
        """
        self._skill = skill

    @strength.setter
    def strength(self, strength):
        """
        Setter for _strength attribute
        """
        self._strength = strength


# testing:
def main():
    """
    Method for testing block
    """
    orc1 = Orcs("Jerry", 4, 3)
    orc2 = Orcs("Jimmy", 3, 5)
    orc1.attack(orc2)
    orc1.saveOrc()


if __name__ == "__main__":
    main()
