
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
# FUNCTION break_examples
#---------------------------
def break_examples():
    # 1. We can break a for loop
    print("-----------------")
    print(" Example 1       ")
    print("-----------------")
    for i in [2,4,8]:
        if i == 4:
            break
        print("i =", i)

    # 2. We can break out of the smallest enclosing for loop
    print("-----------------")
    print(" Example 2       ")
    print("-----------------")
    for i in [2,4,8]:
        for j in "Sun":
            if j == 'u':
                break
            print("i =", i, "j =", j)

    # 3. We can break a while loop
    print("-----------------")
    print(" Example 3       ")
    print("-----------------")
    i = 1
    while i <= 8:
        i *= 2
        if i == 4:
            break
        print("i =", i)

    # 4. We can break out of the smallest enclosing while loop
    print("-----------------")
    print(" Example 4       ")
    print("-----------------")
    i = 2
    while i <= 8:
        j = 0
        while j < 4:
            j += 1
            if j % 2 == 0:
                break
            print("i =", i, "j =", j)
        i *= 2

# ---------------------------
# FUNCTION continue_examples
# ---------------------------
def continue_examples():
    # 1. We can continue a for loop
    print("-----------------")
    print(" Example 1       ")
    print("-----------------")
    for i in [2,4,8]:
        if i == 4:
            continue
        print("i =", i)

    # 2. We can continue out of the smallest enclosing for loop
    print("-----------------")
    print(" Example 2       ")
    print("-----------------")
    for i in [2,4,8]:
        for j in "Sun":
            if j == 'u':
                continue
            print("i =", i, "j =", j)

    # 3. We can continue a while loop
    print("-----------------")
    print(" Example 3       ")
    print("-----------------")
    i = 1
    while i <= 8:
        i *= 2
        if i == 4:
            continue
        print("i =", i)

    # 4. We can continue out of the smallest enclosing while loop
    print("-----------------")
    print(" Example 4       ")
    print("-----------------")
    i = 2
    while i <= 8:
        j = 0
        while j < 4:
            j += 1
            if j % 2 == 0:
                continue
            print("i =", i, "j =", j)
        i *= 2

#-----------------------
# FUNCTION my_main
#-----------------------
def my_main():
    # 1. We execute the break examples
    print("--------------")
    print("break_examples")
    print("--------------")
    break_examples()

    # 2. We execute the continue examples
    print("-----------------")
    print("continue_examples")
    print("-----------------")
    continue_examples()


#---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
#---------------------------------------------------------------
if __name__ == '__main__':
    my_main()
