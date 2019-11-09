
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

#-----------------------
# GLOBAL VARIABLES
#-----------------------
global a = 2

#-----------------------
# FUNCTION example_1
#-----------------------
def example_1():
    # 1. The scope of a global variable is the entire program section.
    # Thus, the scope of the global variable 'a' includes the function example_1
    i = 1
    if i < a:
        print("i = ", i, "is < than a = ", a)
    else:
        print("i = ", i, "is >= than a = ", a)

# -----------------------
# FUNCTION extra
# -----------------------
def extra():
    x = a
    print(x)
    i = 4
    x = i

# -----------------------
# FUNCTION example_2
# -----------------------
def example_2():
    # 1. A function can define a local variable with name 'a' so as to overwrite the global variable 'a'.
    # Thus, the scope of the global variable 'a' does not include the function example_2.
    # Instead, the local variable 'a' is used.
    a = 1
    i = 1
    if i < a:
        print("i = ", i, "is < than a = ", a)
    else:
        print("i = ", i, "is >= than a = ", a)

# -----------------------
# FUNCTION example_3
# -----------------------
def example_3():
    i = False
    if i == True:
        x = 3
    x = x + 1
    print(x)

#---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
#---------------------------------------------------------------
if __name__ == '__main__':
    example_3()
