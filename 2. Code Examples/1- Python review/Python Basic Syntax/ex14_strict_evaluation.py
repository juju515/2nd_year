
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
# FUNCTION loop
#-----------------------
def loop():
    return loop()

#-----------------------
# FUNCTION return_5
#-----------------------
def return_5():
    return 5

#-----------------------
# FUNCTION second
#-----------------------
def second(n1, n2):
    return n2

#-----------------------
# FUNCTION my_main
#-----------------------
def my_main():
    val1 = second(1+2, return_5())
    print(val1)

    print("------------")

    val2 = second(loop(), 3)
    print(val2)

#---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
#---------------------------------------------------------------
if __name__ == '__main__':
    my_main()

