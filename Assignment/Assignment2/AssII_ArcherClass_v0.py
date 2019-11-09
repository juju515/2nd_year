from Assignment.Assignment2.AssII_HumanClass_v0 import Humans

class Knight(Humans):
    """
    Creating the class Humans
    Humans have the following attributes:
        - name       -->   user input
        - weapon     -->   always True
        - skill      -->   int: 1 to 10
        - kingdom    -->   user input string
        - archers    -->   instances of the class archers
    """
    def __init__(self, name, skill, kingdom, archers, weapon):
        Humans.__init__(self, name, skill, weapon)
        self._archers = archers

    # TODO - do the whole thing
