
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

# ----------------------------
# FUNCTION my_main
# ----------------------------
def my_main():
    # 1. We create a list
    my_list = [3, 5, 7, 11]
    print(my_list)

    # 2. The operation reverse does the job
    my_list.reverse()
    print("Sorted list = ", my_list)

#---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
#---------------------------------------------------------------
if __name__ == '__main__':
    my_main()
