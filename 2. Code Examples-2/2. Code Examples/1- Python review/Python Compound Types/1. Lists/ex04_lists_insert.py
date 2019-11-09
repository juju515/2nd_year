
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

    # 2. We can use append to insert at the very last position
    my_list.append(8)
    print(my_list)

    # 3. We can use insert so as to insert a value at a concrete index. In this case, we insert the value 5 at the position 0.
    my_list.insert(0, 6)
    print(my_list)

    # 4. In the case of the insert operation, there is no problem on picking an index out of the range of the list,
    # it will include it at the very end, just as if we were using the 'append' function.
    my_list.insert(18, 9)
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
