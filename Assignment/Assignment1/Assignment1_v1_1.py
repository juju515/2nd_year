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
    Creating the class Orks
    Orks have the following attributes:
        - name       -->   user input
        - weapon     -->   True or False (if no input is given: False)
        - skill      -->   random: 1 to 10
        - strength   -->   random: 1 to 10
    """

    # constructor:
    def __init__(self, name, weapon=False):
        """
        constructor for class Orks
        """
        skill = random.uniform(1, 10)
        strength = random.uniform(1, 10)

        self._name = name
        self._weapon = weapon
        self._skill = skill
        self._strength = strength

    # string representation:
    def __str__(self):
        """
        For Printing the information on the Orcs
        """
        return ("\r Name: %s \n Weapon: %s \n Skill: %.1f \n Strength: %.1f" %
                (self._name, self.weapon, self.skill, self.strength))            # prints the class instance

    # orks fighting function (overloading with ">")
    def __gt__(self, other):
        if self.weapon is False and other.weapon is False:                        # if both orks have NO weapon
            if self.strength > other.strength:                                    # fight with str
                self.skill = self.skill * 1.05
                return print("The winner is: ", self.name, " >>> skill + 5%")
            else:
                other.skill = other.skill * 1.05
                return print("The winner is: ", other.name, " >>> skill + 5%")
        elif self.weapon is True and other.weapon is True:                        # if both orks have weapons
            if self.skill > other.skill:                                          # fight with skill
                self.skill = self.skill * 1.05
                return print("The winner is: ", self.name, " >>> skill + 5%")
            else:
                other.skill = other.skill * 1.05
                return print("The winner is: ", other.name, " >>> skill + 5%")
        elif self.weapon is True and other.weapon is False:                       # if only "self" ork has a weapon
            self.skill = self.skill * 1.05
            return print("The winner is: ", self.name, " >>> skill + 5%")
        elif self.weapon is False and other.weapon is True:                       # is only "other" ork has a weapon
            other.skill = other.skill * 1.05
            return print("The winner is: ", other.name, " >>> skill + 5%")
        else:
            return print("Both Orks lost.")                                         # if it's a draw

    def saveOrk(self):
        with shelve.open("orc"+self._name) as shelf:
            shelf["nameKey"] = self.name
            shelf["weaponKey"] = self.weapon
            shelf["strengthKey"] = self.strength
            shelf["skillKey"] = self.skill

    # getters:
    @property
    def name(self):
        """
        Getter for _name attribute
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
    # testing the constructor
    print("Testing the class constructor: ")
    ork1 = Orcs("Jack")

    # testing the __str__
    print(ork1)

    print("_____________________" * 4,
          "\nAfter using Decorators: ")

    ork1.name = "Jerry"
    print(ork1.name)
    ork1.weapon = False
    print(ork1.weapon)
    ork1.skill = 4.2
    print(ork1.skill)
    ork1.strength = 6.4
    print(ork1.strength)

    print("_____________________" * 4,
          "\nFight Simmulator aka Colosseum Arena aka Flavian Amphitheatre: \n")

    # testing the fight if both weapon is False
    print("Orks fight with NO weapons > ")
    ork2 = Orcs("Johnny")
    ork3 = Orcs("Jimmie")
    print(ork2.name, "str: ", ork2.strength)
    print(ork3.name, "str: ", ork3.strength)
    ork2 > ork3

    # testing the fight if both weapon is True
    print("\nOrks fight with weapons > ")
    ork2.weapon = True
    ork3.weapon = True
    print(ork2.name, "skill: ", ork2.skill)
    print(ork3.name, "skill: ", ork3.skill)
    ork2 > ork3

    # testing the fight if only one weapon is True
    print("\nOnly 'self' ork has a weapon > ")
    ork2.weapon = False
    print(ork2.name, "has a weapon ", ork2.weapon)
    print(ork3.name, "has a weapon ", ork3.weapon)
    ork2 > ork3

    print("\nOnly 'other' ork has a weapon > ")
    ork2.weapon = True
    ork3.weapon = False
    print(ork2.name, "has a weapon ", ork2.weapon)
    print(ork3.name, "has a weapon ", ork3.weapon)
    ork2 > ork3

    # testing the skills increase after the fight
    print("_____________________" * 4,
          "\nSkills reward check: \n")
    ork4 = Orcs("James")
    ork5 = Orcs("Jacob")
    ork4.weapon = True
    ork5.weapon = False
    print("Starting stats > \n", ork4)
    print("\n", ork5, "\n")
    ork4 > ork5
    print("\nEnd stats > \n", ork4)
    print("\n", ork5, "\n")
    
    # what the program should actually print
    print("_____________________" * 4, "\n",
          "Program should actually print: ", "\n" * 7)
    ork6 = Orcs("Jimmy")
    ork7 = Orcs("Timmy")
    ork6 > ork7

    ork4.saveOrk()


if __name__ == "__main__":
    main()
