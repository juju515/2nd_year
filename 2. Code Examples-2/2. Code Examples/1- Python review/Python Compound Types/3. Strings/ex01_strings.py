
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
    # 1. We create an empty tuple
    my_tuple1 = ()

    # 2. We create a second tuple
    print("-----------------------------")
    my_tuple2 = (3, 4.5, True, [1,2])
    print(my_tuple2)

    # 3. We can access to the elements of the tuple in the same way we access to the lists ones.
    print("-----------------------------")
    print(my_tuple2[2])

    # 4. We can get the length of the tuple
    print("-----------------------------")
    print(len(my_tuple2))

    # 5. We can check if an element belongs to a tuple
    print("-----------------------------")
    value1 = 4.5 in my_tuple2
    value2 = 11 in my_tuple2
    print(value1)
    print(value2)

    # 6. Max of a tuple
    print("-----------------------------")
    my_tuple3 = (3, 9, 7, 5)
    value1 = max(my_tuple3)
    print(value1)

    # 7. Number of appearances
    print("-----------------------------")
    my_tuple4 = (3, 9, 3, 5)
    value1 = my_tuple4.count(3)
    print(value1)
    value2 = my_tuple4.count(11)
    print(value2)

    # 8. Find the index
    print("-----------------------------")
    my_tuple4 = (3, 9, 3, 5)
    value1 = my_tuple4.index(9)
    print(value1)

    # 9. Tuple comprehension
    print("-----------------------------")
    my_tuple4 = (3, 9, 3, 5)
    value1 = [x for x in my_tuple4 if x > 4]
    print(value1)

#---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
#---------------------------------------------------------------
if __name__ == '__main__':
    my_main()
