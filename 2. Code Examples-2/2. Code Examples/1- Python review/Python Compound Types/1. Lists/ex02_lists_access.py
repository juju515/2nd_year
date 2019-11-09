
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

    # 2. We can access to a single element of the list by using list[position]
    if (len(my_list) > 1):
        item = my_list[1]
        print("Item at my_list[1] = ", item)
    else:
        print("Sorry, the list does not have at least two elements")

    # 3. If we try to access to an element out of the range of the list, then the program will just raise an error.
    # Thus, in order to avoid that, we previously use len(list) so as to compute the length of the list
    if (len(my_list) > 3):
        item = my_list[3]
        print("Item at my_list[3] = ", item)
    else:
        print("Sorry, the list does not have at least four elements")

    # 4. We can access to multiple elements of the list by using [ : ]
    sub_list1 = my_list[0:2]
    print("sub-list1 of", my_list, "at range of indexes [0:2] = ", sub_list1)

    # As we can see, in the case of the [ : ] operation, there is no problem if the elements we are looking for are out of the range of the list.
    # If this is the case, then the operation [ : ] just returns nothing for each element out of the range of the list.
    print("Sub-list of", my_list, "at range of indexes [1:5] = ", my_list[1:5])

    sub_list3 = my_list[3:18]
    print("Sub-list of", my_list, "at range of indexes [3:18] = ", sub_list3)

#---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
#---------------------------------------------------------------
if __name__ == '__main__':
    my_main()
