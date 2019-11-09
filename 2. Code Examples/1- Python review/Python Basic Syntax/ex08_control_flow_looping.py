
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

#---------------------------
# FUNCTION for_examples
#---------------------------
def for_examples():
    # 1. We can iterate in the elements of a list
    print("-----------------")
    print(" Example 1       ")
    print("-----------------")
    for i in [2,4,8]:
        print("i =", i)
        print("i + 1 =", i + 1)

    # 2. We can iterate in the characters of a String
    print("-----------------")
    print(" Example 2       ")
    print("-----------------")
    for j in enumerate("Hello"):
        print("j =", j)

    # 3. We can iterate in a range, which is an immutable sequence type
    # 3.1. All numbers in the interval (except the latter one) are tried.
    print("-----------------")
    print(" Example 3.1     ")
    print("-----------------")
    my_list = range(1,5)
    print (my_list)
    for k in my_list:
        print("k =", k)

    # 3.2. A range can also set an increase step for each iteration
    print("-----------------")
    print(" Example 3.2     ")
    print("-----------------")
    for l in range(2, 10, 2):
        print("l =", l)

# ---------------------------
# FUNCTION while_examples
# ---------------------------
def while_examples():
    # 1. Fixed true expression:
    # WARNING: This while loop will make the program hang up, or enter an infinite loop, as the expression True always evaluates to the value True.
    print("-----------------")
    print(" Example 1       ")
    print("-----------------")
    #while True:
    #    print("A")

    # 2. Fixed false expression:
    # This while loop is never executed, as the expression False always evaluates to the value False
    print("-----------------")
    print(" Example 2       ")
    print("-----------------")
    while False:
        a = 3
        print("B")

    # 3. Variable expression: Here the if block executes only if the expression x > 2 is reduced to the value True.

    # However, here the expression x > 2 is not fixed, it depends on a variable x.
    # In this case, as we previously assigned x to the value 5, the expression x > 2 evaluates to true.
    # Then, within the loop, the value of x is decreased by one, so the while loop will be evaluated three times:
    # i) When x = 5
    # ii) When x = 4
    # iii) When x = 3
    # Finally, when x = 2, the condition evaluates to False, and the block is not executed again.
    print("-----------------")
    print(" Example 3       ")
    print("-----------------")
    x = 5
    while x > 2:
        print("C")
        x = x - 1

    # 4. Complex expressions: Here the if block executes only if the expression x > 0 and x < 3 evaluates to True
    # That is, it evaluates to True is the value x is assigned to is within the interval (0,3)
    # As x currently takes the value 2, the while loop will be evaluated twice:
    # i) When x = 2
    # ii) When x = 1
    # Finally, when x = 0, the condition evaluates to False, and the block is not executed again.
    print("-----------------")
    print(" Example 4       ")
    print("-----------------")
    while x > 0 and x < 3:
        i = 4
        print("D")
        x -=  1

# ------------------------------
# FUNCTION nested_loop_examples
# ------------------------------
def nested_loop_examples():
    # 1. We can nest as many for loops as we want
    print("-----------------")
    print(" Example 1       ")
    print("-----------------")
    for i in range(1,3):
        for j in "Sun":
            for k in [True, False]:
                print(i, j , k)

    # 2. We can nest as many while loops as we want
    print("-----------------")
    print(" Example 2       ")
    print("-----------------")
    i = 1
    while i < 5:
        j = 1
        while j < 3:
            print(i + j)
            j += 1
        i += 1

#-----------------------
# FUNCTION my_main
#-----------------------
def my_main():
    # 1. We execute the for examples
    print("------------")
    print("for_examples")
    print("------------")
    for_examples()

    # 2. We execute the while examples
    print("--------------")
    print("while_examples")
    print("--------------")
    while_examples()

    # 3. We execute the nested_loop examples
    print("--------------")
    print("nested_loop_examples")
    print("--------------")
    nested_loop_examples()

#---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
#---------------------------------------------------------------
if __name__ == '__main__':
    my_main()
    #nested_loop_examples()