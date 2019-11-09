
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
# IMPORTS
#------------------------------
import math
import sys

#------------------------------
# FUNCTION log_of_arguments
#------------------------------
def log_of_arguments():
    # 0.When calling a program from command line, the argument sys.argv[0]
    #is always the name of the program (in this case: exp4_imports.py).
    print(sys.argv[0])
    # 1. Get the first argument and convert it from String to int
    num = sys.argv[1]
    i_num = int(num)

    # 2. Get the second argument and convert it from String to int
    base = sys.argv[2]
    i_base = int(base)

    # 3. Compute the logarithm and print it
    result = math.log(i_num, i_base)
    print("Result = ", result)


#---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
#---------------------------------------------------------------
if __name__ == '__main__':
    log_of_arguments()
