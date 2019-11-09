
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
    my_list = [3, 5, 7]
    print(my_list)

    # 2. The operation index computes the index of an element in the list
    value_1 = my_list.index(5)

    # 3. However, if the element does not belong to the list, then the program will just raise an error.
    # Thus, in order to avoid that, we previously use the membership 'in' operator, so as to guarantee its membership before applying the operator
    if (11 in my_list):
        value_2 = my_list.index(11)
    else:
        print("Sorry, the element 11 does not belong to the list")

#---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
#---------------------------------------------------------------
if __name__ == '__main__':
    my_main()
