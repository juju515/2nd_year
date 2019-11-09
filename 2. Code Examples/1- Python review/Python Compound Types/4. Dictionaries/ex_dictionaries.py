
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




#-----------------------
# FUNCTION my_main
#-----------------------
def my_main():

    #----
    #1. Create a new dictionary
    #----
    print("----------------------------------")
    print("Create a new dictionary")
    print("----------------------------------")
    my_dict = { "Name" : "Messi", "Age" : 29, "Goals" : 465}
    print(my_dict)

    #----
    #2. Access to an entry
    #----
    print("----------------------------------")
    print("Access to a dictionary entry")
    print("----------------------------------")
    val = my_dict["Age"]
    print(val)

    #----
    #3. Create new entry
    #----
    print("----------------------------------")
    print("Create new dictionary entry")
    print("----------------------------------")
    my_dict["Team"] = "FC_Barcelona"
    print(my_dict)

    #----
    #4. Update existing entry
    #----
    print("----------------------------------")
    print("Update existing dictionary entry")
    print("----------------------------------")
    my_dict["Age"] = 30
    print(my_dict)

    #----
    #5. Delete existing entry
    #----
    print("----------------------------------")
    print("Delete existing dictionary entry")
    print("----------------------------------")
    del my_dict["Age"]
    print(my_dict)

    #----
    #6. Clear all entries
    #----
    print("----------------------------------")
    print("Clear all dictionary entries")
    print("----------------------------------")
    my_dict.clear()
    print(my_dict)

    #----
    #7. Is key in dictionary
    #----
    print("----------------------------------")
    print("Check if key is in our dictionary")
    print("----------------------------------")
    my_dict2 = { "Name" : "Messi", "Age" : 29, "Goals" : 465}
    b1 = "Name" in my_dict2
    print(b1)
    b2 = "Team" in my_dict2
    print(b2)

    #----
    #8. Get keys and values
    #----
    print("----------------------------------")
    print("Get keys and values of our dictionary")
    print("----------------------------------")
    l1 = my_dict2.keys()
    print(l1)
    l2 = my_dict2.values()
    print(l2)

#---------------------------------------------------------------
#           PYTHON EXECUTION
# This is the main entry point to the execution of our program.
# It provides a call to the 'main function' defined in our
# Python program, making the Python interpreter to trigger
# its execution.
#---------------------------------------------------------------
if __name__ == '__main__':
    my_main()
