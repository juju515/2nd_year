
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

    # 2. We print the list content before modifying it
    print(my_list)

    # 3. Please note that each element in the list is nothing but a variable.
    # Thus, we can modify each list element in the same way we modify a variable.
    if (len(my_list) >= 2):
        my_list[1] = 7
        print(my_list)
    else:
        print("Sorry, the list does not have at least two elements")

    if (len(my_list) >= 3):
        my_list[2] = my_list[2] + 1
        print(my_list)
    else:
        print("Sorry, the list does not have at least three elements")

    # 4. If we try to access to an element out of the range of the list, then the program will just raise an error.
    # Thus, in order to avoid that, we previously use len(list) so as to compute the length of the list
    if (len(my_list) >= 7):
        my_list[6] = 8
        print(my_list)
    else:
        print("Sorry, the list does not have at least seven elements")

    my_list[6] = 8

#---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
#---------------------------------------------------------------
if __name__ == '__main__':
    my_main()
