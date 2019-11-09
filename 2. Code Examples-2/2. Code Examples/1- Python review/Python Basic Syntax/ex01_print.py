
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
# FUNCTION print_examples
#---------------------------
def print_examples():
    # 1. Print a message by the standard output
    print('Hello World!')

    # 2. We can see that we can use double quotes as well
    print("Hello World again!")

    # 3. Print a message consisting on three sub-messages
    # As we can see, the separation between the sub-messages is a single space
    print("First part", "followed by second", "and finish with the last one")

    # 4. Modify the separation space
    # As we can see, the separation between the sub-messages is now defined by us
    # print("First part", "followed by second", "and finish with the last one", sep='^^^')

    # 5. Modify so as to not to have end line at the end
    # As we can see, the first print does not finish with a new line
    #print("Hello, ", end='')
    print("how are you?")

    # 6. Print to a file, rather than to the standard output
    # We will see more on this later on
    f = open('my_file.txt', 'w')
    #f = open('/Users/lcliment/Desktop/my_file.txt', 'w')
    print("Hello, now I'm printing to a file", file=f)

    # 7. Finally, besides printing to the standard output, we can also read from the standard input.
    # This allows to have some interaction with the user, which can pass info in the middle of the program execution.
    var = input("Please enter something: ")
    print("You entered", var)

#---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
#---------------------------------------------------------------
if __name__ == '__main__':
    print_examples()

