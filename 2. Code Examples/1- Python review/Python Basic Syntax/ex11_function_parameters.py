
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
# FUNCTION no_param
#---------------------------
def no_param():
    print("Hello")

#---------------------------
# FUNCTION one_param
#---------------------------
def one_param(message):
    # This function has a single formal parameter, called 'message'.
    # This parameter is nothing but a variable. And remember, all variables in Python have to have a value.
    # Which value is the variable 'message' assigned to?
    # This is resolved each time the function is called.
    # On each call to the function, the control is transfer to it, and the variable 'message' is assigned to the value the function is called with.

    # 1. Once the function is called and a concrete value is assigned to 'message', the function just prints the value message is assigned to.
    print(message)

#---------------------------
# FUNCTION multiple_params
#---------------------------
def multiple_params(param1, param2, param3):
    # This function has three parameters, or variables: 'param1', 'param2' and 'param3'.

    # 1. 'param1' is expected to receive a Boolean value. If this value is false, nothing is done. But, if the value is true...
    if (param1 == True):
        # 1.1. An i variable iterates in the range 0..param2. Thus, param2 is expected to receive an integer value,
        # which will determine the number of iterations of the for loop.
        for i in range(0, param2):
            # 1.1.1. param3 can be of any type. It can receive a value of any type: An integer, double, boolean, string, tuple, dictionary.
            # Whatever it is passed to it, it just prints it.
            print(param3)

#-----------------------
# FUNCTION my_main
#-----------------------
def my_main():
    # 1. Whereas function no_param is always going to print the fixed message "Hello"
    no_param()
    print("------------")

    # 2. The function one_param can print anything we want.
    # All we need is to call the function with the message we want to write

    # 2.1. We can print a word.
    # 2.1.1. We can call it directly with the word, and the variable 'message' of one_param will be assigned to the word.
    one_param("Bonjour")
    print("--------------")

    # 2.1.2. We can call it with a variable, assigned to the value we want to print.
    x = "Hola"
    one_param(x)
    print("--------------")

    # 2.2. We can print a integer value, or a double
    one_param(3)
    print("--------------")

    y = 4.5
    one_param(y)
    print("--------------")

    # 3. The function multiple params do one thing or another depending on the values it is assigned to

    # 3.1. If first param is True, the amount of loop iterations depends on the second value

    # 3.1.1. Here we go with a first example of it
    multiple_params(True, 3, "Hello")
    print("--------------")

    # 3.1.2. Obviously, same call can be done using variables (assigned to these value) rather than using the values directly
    var1 = True
    var2 = 3
    var3 = "Hello"
    multiple_params(var1, var2, var3)
    print("--------------")

    # 3.1.3. Another example with first param being True, but with a different value for second param
    multiple_params(True, 5, 4.5)
    print("--------------")

    # 3.2. If first parameter is False, then nothing is printed at all
    multiple_params(False, 3, "Hello")
    multiple_params(False, 5, 4.5)

    # 3.3. Finally, if second parameter is not an integer, the function is called, no problem, but it's execution leads to an error, as
    # for i in range(0, param2):
    # can only work is param2 is an integer
    multiple_params(True, "Hola", "Hello")

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
    #multiple_params(True, "Hello", "Hello")

