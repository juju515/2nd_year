import shelve
import Assignment.Assignment1.Assignment1_v1_2 as test

# testing the class:
orc1 = test.Orcs("Timmy")
orc2 = test.Orcs("Jimmy")
print(orc1, "\n" * 2, orc2, "\n")

print(orc1.attack(orc2))



# testing the shelve:
x = shelve.open("orcJimmy")
Jimmy = test.Orcs('moop')
Jimmy.strength, Jimmy.skill = x["strengthKey"], x["skillKey"]
print(Jimmy.strength, Jimmy.skill)
x.close()