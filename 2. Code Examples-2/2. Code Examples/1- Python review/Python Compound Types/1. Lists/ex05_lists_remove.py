
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
    my_list = [11, 5, 3, 7]
    print(my_list)

    del my_list[1:3]
    print(my_list)


    # 1. We can use del[position] to delete a concrete index of the list
    # However, once again, if we try to access to an element out of the range of the list, then the program will just raise an error.
    # Thus, in order to avoid that, we previously use len(list) so as to compute the length of the list
    if (len(my_list) > 2):
        del my_list[2]
    print(my_list)

    # 2. Likewise, we can use delete(value) to remove the first appearance of value in the list.
    # The problem is that, once again, if this value is not in the list, then the program will raise an error.
    # Thus, we can use the function 'in' to check the membership of the value we want to remove
    if 5 in my_list:
        my_list.remove(5)
    print(my_list)

    if 9 in my_list:
        my_list.remove(9)
    print(my_list)

#---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
#---------------------------------------------------------------
if __name__ == '__main__':
    my_main()
