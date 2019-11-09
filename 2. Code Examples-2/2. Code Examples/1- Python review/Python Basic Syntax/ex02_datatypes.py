
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

#----------------------------
# FUNCTION python_datatypes
#----------------------------
def python_datatypes():
    # 1. We assign a to an integer value
    a = 3

    # 2. We assign b to an float value
    b = 3.5

    # 3. We assign c to a Boolean value
    c = True

    # 4. We assign d to an String value
    d = "Hello"

    # 5. We assign e to a list of integer values
    e = [1,2,3,True]

    # 6. We assign f to a tuple of a pair of values, the first one a float and the second one a Boolean
    f = (3.5, True, 1)

    # 7. We assign g to a dictionary or hash table with three entries: 'Name', assigned to a String value; 'Age', assigned to an integer value; 'Goals', assigned to an integer value.
    g = {'Name': "Messi",
         'Age': 29,
         'Goals': 500}

    # 8. We now print the value of each variable, together with the type of the value it is assigned to
    print(a, type(a))
    print(b, type(b))
    print(c, type(c))
    print(d, type(d))
    print(e, type(e))
    print(f, type(f))
    print(g, type(g))

#----------------------------
# FUNCTION type_conversions
#----------------------------
def type_conversions():
    # 1. We assign v1 to a String value
    v1 = '3'
    print('v1 = ', v1, 'type(v1) = ', type(v1))

    # 2. We can also turn a String value into an integer one by casting it
    v1 = int(v1)
    print('v1 = ', v1, 'type(v1) = ', type(v1))

    # 3. By dividing v1 (which value is 3) into 2, the result is the float 1.5
    v2 = v1 / 2
    print('v2 = ', v2, 'type(v2) = ', type(v2))

    # 4. However, we can force the result to be an integer value by casting it
    v2 = int(v1 / 2)
    print('v2 = ', v2, 'type(v2) = ', type(v2))

#---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
#---------------------------------------------------------------
if __name__ == '__main__':
    # 1. We execute the function python_datatypes
    python_datatypes()

    # 2. We execute the function type_conversions
    type_conversions()

