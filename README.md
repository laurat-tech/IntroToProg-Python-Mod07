# IntroToProg-Python-Mod07

```python
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
```

![](docs/Figure1.png)
