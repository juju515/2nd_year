
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
    my_list = []
    for i in range(0, 11):
        my_list.append(i)
    print(my_list)

    # 2. We create a copy of the list by filtering them all
    print("----------------------")
    value1 = [x for x in my_list]
    print(value1)

    # 3. We filter only the odd elements
    print("----------------------")
    value2 = [x for x in my_list if x % 2 == 0]
    print(value2)

    # 4. We filter only the odd elements, and multiply them by 10 before adding them to the new list
    print("----------------------")
    value3 = [10 * x for x in my_list if x % 2 == 0]
    print(value3)

#---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
#---------------------------------------------------------------
if __name__ == '__main__':
    my_main()
