
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

#---------------------------------
# FUNCTION without_try
#---------------------------------
def without_try():
    val = 0 / 0
    return val

#---------------------------------
# FUNCTION with_try
#---------------------------------
def with_try():
    val = 0
    try:
        val = 0 / 0
    except:
        print("Oops, there was an error in the execution of the function")
    return val

#-----------------------
# FUNCTION my_main
#-----------------------
def my_main():
    # 1. We can try to run the code with no exception handling
    with_try()

    # 2. We can run the code with exception handling
    without_try()

#---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
#---------------------------------------------------------------
if __name__ == '__main__':
    my_main()
