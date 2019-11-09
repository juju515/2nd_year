
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
# FUNCTION reverse
# ----------------------------
def reverse(my_list):
    new_list = []
    v1 = len(my_list)
    for i in range(v1-1,-1,-1):
        new_list.append(my_list[i])
    return new_list

#---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
#---------------------------------------------------------------
if __name__ == '__main__':
    #my_main()
    l1 = reverse([3,5,7])
    print(l1)
    l2 = reverse([])
    print(l2)