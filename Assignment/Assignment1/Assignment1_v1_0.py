#!/usr/bin/python

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

import random, shelve


class Orks:
    """
    Creating the class Orks
    Orks have the following attributes:
        - name       >   user input
        - weapon     >   False or True
        - skill      >   1 to 10 random
        - strength   >   1 to 10 random
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
                (self._name, self._weapon, self._skill, self._strength))

    # getters:
    def getName(self):
        """
        Getter for _name attribute
        """
        return self._name

    def getWeapon(self):
        """
        getter for _weapon attribute
        """
        return self._weapon

    def getSkill(self):
        """
        getter for _weapon attribute
        """
        return self._skill

    def getStrength(self):
        """
        getter for _weapon attribute
        """
        return self._strength

    # setters:
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

    def setSkill(self, skill):
        """
        Setter for _skill attribute
        """
        self._skill = skill

    def setStrength(self, strength):
        """
        Setter for _strength attribute
        """
        self._strength = strength

    # properties:
    name = property(getName, setName)
    weapon = property(getWeapon, setWeapon)
    skill = property(getSkill, setSkill)
    strength = property(getStrength, setStrength)

# testing:
def main():
    """
    Method for testing block
    """
    # testing the constructor
    x = Orks("Jack")

    # testing the __str__
    print(x)

    # testing setters
    x.setName("Jerry")
    x.setWeapon(True)
    x.setSkill(3.2)
    x.setStrength(5.5)

    print("_____________________\n"
          "After using Setters: ")

    # testing getters
    print(x.getName())
    print(x.getWeapon())
    print(x.getSkill())
    print(x.getStrength())

    print("_____________________\n"
          "After using Properties: ")

    x.name = "John"
    print(x.name)
    x.weapon = False
    print(x.weapon)
    x.skill = (4.2)
    print(x.skill)
    x.strength = (9.9)
    print(x.strength)




if __name__ == "__main__":
    main()

