import Assignment.Assignment1.Ass1_3types_shite as testO


# testing the constructor
print("Testing the class constructor: ")
orc1 = testO.Orcs("Jack", 3.4, 2.3)


# testing the __str__
print(orc1)

print("_____________________" * 4,
      "\nAfter using Decorators: ")

orc1.setName("Jerry")
print(orc1.getName())
orc1.weapon = False
print(orc1.weapon)
orc1.skill = 4.2
print(orc1.skill)
orc1.strength = 6.4
print(orc1.strength)

print("_____________________" * 4,
      "\nFight Simulator aka Colosseum Arena: \n")


# testing the fight if both weapon is False
print("orcs fight with NO weapons > ")
orc2 = testO.Orcs("Johnny", 3.4, 2.7)
orc3 = testO.Orcs("Jimmie", 6.5, 3.7)
print(orc2.getName(), "str: ", orc2.strength)
print(orc3.getName(), "str: ", orc3.strength)
orc2.attack(orc3)


# testing the fight if both weapon is True
print("\norcs fight with weapons > ")
orc2.weapon = True
orc3.weapon = True
print(orc2.getName(), "skill: ", orc2.skill)
print(orc3.getName(), "skill: ", orc3.skill)
orc2.attack(orc3)

# testing the fight if only one weapon is True
print("\nOnly 'self' orc has a weapon > ")
orc3.weapon = False
print(orc2.getName(), "has a weapon ", orc2.weapon)
print(orc3.getName(), "has a weapon ", orc3.weapon)
orc2.attack(orc3)

print("\nOnly 'other' orc has a weapon > ")
orc3.weapon = True
orc2.weapon = False
print(orc2.getName(), "has a weapon ", orc2.weapon)
print(orc3.getName(), "has a weapon ", orc3.weapon)
orc2.attack(orc3)


# testing the draw
# TODO
print("\nIf orcs are equal and there's no winner > ")
orc2.weapon = False
orc3.weapon = False
orc2.skill = 4
orc2.strength = 6
orc3.skill = 4
orc3.strength = 6
orc2.attack(orc3)


# testing the skills increase after the fight
print("_____________________" * 4,
      "\nSkill reward check: \n")
orc4 = testO.Orcs("Fanny", 5.3, 2.3)
orc5 = testO.Orcs("Benny", 5.3, 2.8)
orc4.weapon = True
orc5.weapon = True
print("Starting stats > \n", orc4)
print("\n", orc5, "\n")
orc4.attack(orc5)
print("\nEnd stats > \n", orc4)
print("\n", orc5, "\n")


# what the program should actually print
print("_____________________" * 4, "\n",
      "Program should actually print: ", "\n" * 7)
orc6 = testO.Orcs("Jimmy", 8.7, 9.5)
orc7 = testO.Orcs("Sammy", 3.4, 5.3)
orc6.attack(orc7)

# testing the shelving function (save all the instances)
orc1.saveOrc()
orc2.saveOrc()
orc3.saveOrc()
orc4.saveOrc()
orc5.saveOrc()
orc6.saveOrc()
orc7.saveOrc()

# TODO
