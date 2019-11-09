
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
    # 1. The operation len computes the length of a list.
    # Let's play with it for two lists: One empty and one non-empty
    my_list_1 = []
    value_1 = len(my_list_1)
    print("The length of my_list_1 = ", value_1)

    my_list_2 = [2, 4, 6]
    value_2 = len(my_list_2)
    print("The length of my_list_2 = ", value_2)

#---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
#---------------------------------------------------------------
if __name__ == '__main__':
    my_main()
