
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
# FUNCTION if_then_examples
#---------------------------
def if_then_examples():
    # 1. Fixed true expression:
    # This block of one line is always executed, as the expression True always evaluates to the value True
    print("-----------------")
    print(" Example 1       ")
    print("-----------------")
    if True == True:
        print("A")

    # 2. Fixed false expression:
    # This block of two lines is never executed, as the expression False always evaluates to the value False
    print("-----------------")
    print(" Example 2       ")
    print("-----------------")
    if False == True:
        a = 3
        print("B")

    # 3. Variable expression: Here the if block executes only if the expression x > 2 is reduced to the value True.

    # However, here the expression x > 2 is not fixed, it depends on a variable x.
    # In this case, as we previously assigned x to the value 3, the expression x > 2 evaluates to true.
    # However, if we had assigned x to the value 1, then the expression x > 2 would have evaluated to false, and the if block would have not been executed.
    print("-----------------")
    print(" Example 3       ")
    print("-----------------")
    x = 3
    if x > 2 == True:
        i = 3
        print("C")

    # 4. Complex expressions: Here the if block executes only if the expression x > 2 and x < 5 evaluates to True
    # That is, it evaluates to True is the value x is assigned to is within the interval (2,5)
    print("-----------------")
    print(" Example 4       ")
    print("-----------------")
    if (x > 2 and x < 5) == True:
        i = 4
        print("D")

#--------------------------------
# FUNCTION if_then_else_examples
#--------------------------------
def if_then_else_examples():
    # 1. Fixed true expression:
    # Here the if block printing A1 is always executed, and the else block printing A2 is never executed.
    print("-----------------")
    print(" Example 1       ")
    print("-----------------")
    if True == True:
        print("A1")
    else:
        print("A2")

    # 2. Fixed false expression:
    # Likewise, here the if block printing B1 is never executed, and the else block printing B2 is always executed.
    print("-----------------")
    print(" Example 2       ")
    print("-----------------")
    if False == True:
        a = 3
        print("B1")
    else:
        a = 4
        print("B2")

    # 3. Variable expression: Here the if block executes only if the expression x > 2 is reduced to the value True, otherwise the else block is executed.

    # However, here the expression x > 2 is not fixed, it depends on a variable x.
    # In this case, as we previously assigned x to the value 3, the expression x > 2 evaluates to true.
    # However, if we had assigned x to the value 1, then the expression x > 2 would have evaluated to false, and the else block would have been executed.
    print("-----------------")
    print(" Example 3       ")
    print("-----------------")
    x = 3
    if x > 2:
        i = 3
        print("C1")
    else:
        i = 4
        print("C2")

    # 4. Complex expressions: Here the if block executes only if the expression x > 2 and x < 5 evaluates to True
    # That is, it evaluates to True is the value x is assigned to is within the range (2,5). Otherwise, it evaluates the else block.
    print("-----------------")
    print(" Example 4       ")
    print("-----------------")
    if x > 2 and x < 5:
        i = 4
        print("D1")
    else:
        i = 5
        print("D2")

# ----------------------------
# FUNCTION nested_if_examples
# ----------------------------
def nested_if_examples():
    # 1. We can nest as many if_then and if_then_else as we want
    print("-----------------")
    print(" Example 1       ")
    print("-----------------")
    a = 6

    if a > 4:
        if a > 6 == True:
            if a > 7:
                print("Case 8")
            else:
                print("Case 7")
        else:
            if a > 5 == True:
                print("Case 6")
            else:
                print("Case 5")
    else:
        if a > 2:
            if a > 3:
                print("Case 4")
            else:
                print("Case 3")
        else:
            if a > 1:
                print("Case 2")
            else:
                print("Case 1")

#-----------------------
# FUNCTION my_main
#-----------------------
def my_main():
    # 1. We execute the if_then examples
    print("----------------")
    print("if_then_examples")
    print("----------------")
    if_then_examples()

    # 2. We execute the if_then_else examples
    print("---------------------")
    print("if_then_else_examples")
    print("---------------------")
    if_then_else_examples()

    # 3. We execute the nested_if examples
    print("------------------")
    print("nested_if_examples")
    print("------------------")
    nested_if_examples()

#---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
#---------------------------------------------------------------
if __name__ == '__main__':
    my_main()
    #if_then_examples()
