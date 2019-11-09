
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
# FUNCTION fun1
#---------------------------
def fun1():
    # 1. The function has a couple of local vairables: x1 and x2
    x1 = 3
    x2 = 4

    # 2. It then prints the String "Hello"
    print("Hello")

    # 3. Finally, it calls to the function fun3
    fun3()

#---------------------------
# FUNCTION fun2
#---------------------------
def fun2():
    # 1. The function defines a local variable: z
    z = False

    # 2. It then prints the String "Hola"
    print("Hola")

# ---------------------------
# FUNCTION fun3
# ---------------------------
def fun3():
    # 1. The function defines a local variable: y
    y = "Bonjour"

    # 2. It then prints the value of the variable
    print(y)

    # 3. Finally, it calls to the function fun2
    fun2()

#-----------------------
# FUNCTION my_main
#-----------------------
def my_main():
    # 1. The function first calls to the function fun1
    fun1()

    # 2. It then calls to the function fun3
    fun3()

#---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
#---------------------------------------------------------------
if __name__ == '__main__':
    # 1. The execution of the Python program first calls to the function my_main
    my_main()

    #2. Then it does nothing else. The execution has then finished.
