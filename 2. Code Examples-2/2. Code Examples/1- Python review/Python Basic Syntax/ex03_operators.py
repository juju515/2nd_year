
#--------------------------------------------------------
#           PYTHON PROGRAM
# Here is where we are going to define our set of...
# - Imports
# - Global Variables
# - Functions
# ...to achieve the functionality required.
# When executing > python 'this_file'.py in a terminal,
# the Python interpreter will load our program,
# but it will execute nothing yet.
#--------------------------------------------------------

#------------------------------
# FUNCTION arithmetic_examples
#------------------------------
def arithmetic_examples():
    add = 6 + 3
    print("add = ", add)
    sub = 6 - 3
    print("sub = ", sub)
    mul = 6 * 3
    print("mul = ", mul)
    div = 6 / 3
    print("div = ", div)
    mod = 6 % 3
    print("mod = ", mod)
    exp = 6 ** 3
    print("exp = ", exp)

#------------------------------
# FUNCTION relational_examples
#------------------------------
def relational_examples():
    equal = 6 == 3
    print("equal = ", equal)
    different = 6 != 3
    print("different = ", different)
    greater = 6 > 3
    print("greater = ", greater)
    greater_equal = 6 >= 3
    print("greater_equal = ", greater_equal)
    lower = 6 < 3
    print("lower = ", lower)
    lower_equal = 6 <= 3
    print("lower_equal = ", lower_equal)

#---------------------------
# FUNCTION logical_examples
#---------------------------
def logical_examples():
    and_example = 6 > 0 and 0 > 2
    print("and_example = ", and_example)
    or_example = 6 > 10 or 3 > 0
    print("or_example = ", or_example)
    not_example = not 6 > 5
    print("not_example = ", not_example)

#----------------------------
# FUNCTION operator_examples
#----------------------------
def operator_examples():
    arithmetic_examples()
    relational_examples()
    logical_examples()

#---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
#---------------------------------------------------------------
if __name__ == '__main__':
    operator_examples()
