
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
# FUNCTION return_nothing
#---------------------------
def return_nothing(x):
    x = x + 1

#---------------------------
# FUNCTION return_one_value
#---------------------------
def return_one_value(x):
    x = x + 1

    # 1. Before finishing, the function can return the value of a variable
    return x

#----------------------------------
# FUNCTION return_multiple_values
#----------------------------------
def return_multiple_values(x):
    y = x + 1
    z = "Hello"
    t = True

    # 1. Before finishing, the function can return the value of several variables
    return (y, z, t)

#-----------------------
# FUNCTION my_main
#-----------------------
def my_main():
    # 1. We create an integer variable and print its value
    var1 = 3
    return_nothing(var1)
    print(var1)

    print("------------")

    # 2. We can assign to a variable the value returned to the function
    new_var = 5
    new_var = return_one_value(var1)
    print(new_var)

    print("------------")

    # 3. We can even assign the value returned to the same variable we are calling the function with
    print(var1)
    var1 = return_one_value(var1)
    print(var1)

    print("------------")

    # 4. We can assign to variables the values returned by a function
    (v1, v2, v3) = return_multiple_values(var1)
    print(v1)
    print(v2)
    print(v3)

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

