
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
# FUNCTION variable_examples
#------------------------------
def variable_examples():
    # 1. We define a couple of variables, assign values to them and print them
    x = 2
    y = 5
    print("The value of x = ", x, ", y = ", y)

    # 2. We modify the variables by assigning them to new expressions
    x = x + 1
    y = y + x
    print("x = ", x, ", y = ", y)
   #y = y + z

    # 3. We make a mistake by trying to use a variable not previously defined
    #x = x + z

    # 4. We can check the type of a variable and change it
    print(y, ", ", type(y))

    y = 3 > 0
    print(y, ", ", type(y))

    y = str(y)
    print(y, ", ", type(y))

#---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
#---------------------------------------------------------------
if __name__ == '__main__':
    variable_examples()
