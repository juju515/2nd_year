"""
CS2513 -  Intermediate Programming
_______________________________________

Assignment 1 - OOP
Part 1.b : Inheritance
(W07-W09) - 10 marks
_______________________________________

Name:           Ozzak Jure Matic
Student num:    118743625

"""

class Character:
    """
    Creating the class Character
    Orcs have the following attributes:
        - name       -->   user input
        - weapon     -->   True or False (if no input is given: False)
        - skill      -->   int: 1 to 10
    """

    def __init__(self, name, skill, weapon):
        """
        constructor for class Character
        """
        self.name = name
        self.weapon = weapon
        self.skill = skill


    # craracter is greater than function (overloading with ">")
    def __gt__(self, other):
        draw = "It's a draw!"
        if self.weapon is False and other.weapon is False:                        # if both char have NO weapon
            return self.strength > other.strength                                 # check the strength stats
        elif self.weapon is True and other.weapon is True:                        # if both char have weapons
            return self.skill > other.skill                                       # check the skill stats
        elif self.weapon is True and other.weapon is False:                       # if only "self" char has a weapon
            return True
        elif self.weapon is False and other.weapon is True:                       # is only "other" char has a weapon
            return False
        else:
            return print(draw)                                                    # TODO - if it's a draw

    # attack function:
    def attack(self, opponent):
        if self > opponent:                                                       # if __gt__ returns True
            self.skill *= 1.05                                                    # increase the self.skill by 5%
            print(self.name, "won the fight and was rewarded +5% skill")          # and print "self" won
        else:                                                                     # if __gt__ returns False
            opponent.skill *= 1.05                                                # increase the other.skill by 5%
            print(opponent.name, "won the fight and was rewarded +5% skill")      # and print "other" won

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
        if skill < 0:                                                             # making sure skill is > 0 and < 10
            return False
        if skill > 10:
            return False
        else:
            self._skill = skill


# testing
def main():
    pass

if __name__ == "__main__":
    main()