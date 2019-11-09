
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

#---------------------------
# FUNCTION parameter_by_value
#---------------------------
def parameter_by_value(x):
    x = x + 1

#---------------------------
# FUNCTION parameter_by_reference
#---------------------------
def parameter_by_reference(x):
    x[0] = x[0] + 1

#-----------------------
# FUNCTION my_main
#-----------------------
def my_main():
    # 1. We create and integer variable and print its value
    var1 = 3
    print(var1)

    # 2. Now we call to the function parameter_by_value with var1, where var1 is passed by value
    parameter_by_value(var1)

    # 3. We now print the value of var1, and we see it has not been modified.
    # Why? Because in the function parameter_by_value, the parameter 'x' is a new variable, which is assigned to the value var1 has.
    # Thus, 'var1' and 'x' are different variables. If we modify 'x', we do not modify 'var1'.
    print(var1)

    print("------------")

    # 4. We create a list of integers variable and print its value
    var2 = [5,5,5]
    print(var2)

    # 5. Now we call to the function parameter_by_reference with var2, where var2 is passed by reference
    parameter_by_reference(var2)

    # 6. We now print the value of var2, and we see it has indeed been modified.
    # Why? Because in the function parameter_by_reference, the parameter 'x' is not a new variable, but the proper var2 it is called with.
    # Thus, 'var2' and 'x' are not different variables, they are the same one indeed. Thus, if we modify 'x', we do indeed modify 'var2'.
    print(var2)

#---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
#---------------------------------------------------------------
if __name__ == '__main__':
    # 1. The execution of the Python program first calls to the function my_main
    my_main()

