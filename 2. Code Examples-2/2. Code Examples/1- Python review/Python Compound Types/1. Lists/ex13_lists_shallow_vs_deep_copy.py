
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
    my_list = [1, 2, 3]
    print(my_list)

    # 2. We create two copies, one shallow and one deep
    shallow_list1 = my_list
    deep_list2 = my_list[:] 
    # [:] is the syntax for every element in the list

    # 3. We modify the two variables
    shallow_list1[0] = 5
    deep_list2[1] = 7

    # 4. We print the lists content
    print(shallow_list1)
    print(deep_list2)
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
