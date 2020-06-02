# ------------------------------------------------- #
# Title: Assignment07
# Description: A simple demo of error handling and pickling
# ChangeLog: (Who, When, What)
# Laura Truong,<5.27.2020,Created Script, added code for pickling
#Laura Truong,<5.28.2020, Tested code for pickling
#Laura Truong,<5.28.2020, Added some code for error handling for a filenotfounderror
# ------------------------------------------------- #


# Data -------------------------------------------- #
import pickle  # This imports code from another code file!
import sys # Import module sys to get the type of exception.
lstBucket = ['Skydiving', 'Hot Air balloon'] # Bucketlist of items that end user will add on to

# Processing -------------------------------------- #
def save_data_to_file(list_of_data): #Writes data in binary to the file.
    with open("BucketList.dat", "wb") as AppData: #Opens file and names it Bucketlist
        print('You typed in', list_of_data) #Tells user what they entered
        pickle.dump(list_of_data, AppData) #Writes pickled obj to the open file
        AppData.close() #Closes the file

def read_data_from_file(): #Reads data in binary to the file.
    with open("BucketList.dat", "rb") as AppData:
        list_of_data = pickle.load(AppData)
        AppData.close()
        return list_of_data

# Presentation ------------------------------------ #
# Get bucketlist item from user, then return the input
def UserInput():
    strItem = str(input("Enter a bucketlist item: ")) #Asks the user to enter an item
    return strItem #Returns the input


#Error Handling------------------------------------ #
try:
    fileData = read_data_from_file() #reads the data
except FileNotFoundError as e: #FileNotFoundError exception if it is end user's first time opening
    print('File not found. You have no data to read since this is your first time opening the program.')
    fileData = lstBucket
except pickle.UnpicklingError as e: #Raised when there is a problem unpickling an object
    print('File contains corrupted data')
    sys.exit(1)

try:
    fileData.append(UserInput()) #Adding what the user enters to the list
    save_data_to_file(fileData) #Writing data to the file
except Exception as e:  # Tells the end user what the exception error is if not defined.
    print("Oops!", e.__class__, "occurred.") #Prints the exception error so the end user can see it.





