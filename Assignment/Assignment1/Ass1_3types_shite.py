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

import random
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
                (self.getName(), self.weapon, self.skill, self.strength))              # prints the class instance

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
            print(self.getName(), "won the fight and was rewarded +5% skill")          # and print "self" won
        else:                                                                     # if __gt__ returns False
            opponent.skill *= 1.05                                                # increase the other.skill by 5%
            print(opponent.getName(), "won the fight and was rewarded +5% skill")      # and print "other" won

    # function for saving instances to the shelve:
    def saveOrc(self):
        with shelve.open("orc_"+self.getName()) as shelf:                            # opening/closing the shelve with "with"
            shelf["nameKey"] = self.getName()                                        # saving the instance attributes
            shelf["weaponKey"] = self.weapon                                    # under [nameKey], [weaponKey],
            shelf["strengthKey"] = self.strength                                # [strengthKey] and [skillKey]
            shelf["skillKey"] = self.skill

    # getter:
    def getName(self):
        """
        Getter for _name attribute
        """
        return self._name

    # declared property:
    def getWeapon(self):
        """
        getter for _weapon attribute
        """
        return self._weapon

    #decorator
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

    # setter:
    def setName(self, name):
        """
        Setter for _name attribute
        """
        self._name = name

    def setWeapon(self, weapon):
        """
        Setter for _weapon attribute
        """
        self._weapon = weapon
    weapon = property(getWeapon, setWeapon)


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
    orc1 = Orcs("Jerry")
    orc2 = Orcs("Jimmy")
    orc1.attack(orc2)
    orc1.saveOrc()


if __name__ == "__main__":
    main()
