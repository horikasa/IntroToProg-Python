# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# HOrikasa, 11/15/2021, Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
openFile = open(objFile, 'r')
for row in openFile:
    lstRow = row.split(',')
    dicRow = {'Task': lstRow[0], 'Priority': lstRow[1]}
    lstTable.append(dicRow)
openFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if strChoice.strip() == '1':
        print('Current Data:')
        for row in lstTable:
            print(row['Task'] + ', ' + row['Priority'].strip())
        continue

    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        strTask = input('Please enter task: ')
        strPriority = input('Please assign a priority for this task ["high", "medium", "low"]: ')
        dicRow = {'Task': strTask, 'Priority': strPriority}
        lstTable.append(dicRow)
        print('Your new task has been added!!')
        continue

    # Step 5 - Remove a new item from the list/Table
    elif strChoice.strip() == '3':
        print('Your current task list is:\n')
        for row in lstTable:
            print(row['Task'] + ', ' + row['Priority'].strip())
        strRemove = input('\nWhich task would you like to remove? ')
        for row in lstTable:
            if strRemove.lower() in row['Task'].lower():
                lstTable.remove(row)
                print('\n' + strRemove + ' has been removed from your task list.')
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif strChoice.strip() == '4':
        openFile = open(objFile, 'w')
        for row in lstTable:
            openFile.write('\n' + row['Task'] + ', ' + row['Priority'])
        openFile.close()
        print('Your data has been saved!\n')
        continue

    # Step 7 - Exit program
    elif strChoice.strip() == '5':
        print('See you next time!!')
        break  # and Exit the program
