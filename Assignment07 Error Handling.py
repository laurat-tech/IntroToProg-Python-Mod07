# ------------------------------------------------- #
# Title: Assignment07
# Description: A simple demo of error handling
# ChangeLog: (Who, When, What)
# Laura Truong,<5.27.2020,Created Script, added code for error handling
#Laura Truong,<5.28.2020, Tested code and changed code from static data to allowing the end user to enter a number
#Laura Truong,<5.28.2020, Added exception in exception handling to print what error the user ran into for reference.
#Laura Truong,<5.28.2020, Tested code for finalization
# ------------------------------------------------- #

import sys #Import module sys to get the type of exception.

randomList = input("Enter a number to find its reciprocal in decimal form: ") #Prompts user to enter a number.

for entry in randomList:
    try:
        print("The entry is", entry) #Prints what  the user entered.
        r = 1/int(entry) #Finds the reciprocal of the input.
        break #Ends the for loop.
    except ValueError as e: #Does not allow the user to enter anything other than a number.
        print("You must enter a number.")

    except ZeroDivisionError as e: #Does not allow user to enter a number less than 1.
        print("You cannot divide by zero. ")

    except Exception as e: #Tells the end user what the exception error is if not defined.
        print("Oops!", e.__class__, "occurred.")

print("The reciprocal of", entry, "is", r)