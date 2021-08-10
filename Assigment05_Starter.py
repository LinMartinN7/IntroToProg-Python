# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# LMartin, 8.3.2021, Saved file to PC and added code for Step 1 and 3.
# LMartin, 8.4.2021, Added Code for Step 7 and started code for Step 4.
# LMartin, 8.8.2021, Added code for Step 6.
# LMartin, 8.9.2021, Added code for Step 4 and 5.
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
objFile = open("ToDoList.txt", "r")
for row in objFile:
    lstRow = row.split(',')
    dicRow = {'Task': lstRow[0], 'Priority': lstRow[1].strip()}
    lstTable.append(dicRow)
objFile.close()

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
    if (strChoice.strip() == '1'):
        print("----- The current items in the To-Do List are: -----")
        for objRow in lstTable:
            print(objRow["Task"] + "," + objRow["Priority"])
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        print("\nType in a task and priority for the To-Do List.")
        strTask = str(input("\nEnter a new task to do: "))
        strPriority = str(input("Enter the task's priority (high, medium, low): ")).strip()
        if strPriority == "high" or strPriority == "medium" or strPriority == "low":
            dicRow = {"Task": strTask, "Priority": strPriority}
            lstTable.append(dicRow)
            print("\nThe Task -|" + strTask + "|- and priority -|" + strPriority + "|- have been added.")
        else:
            print("Invalid Input. Please enter 'high', 'medium', or 'low' for priority.")
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        while(True):
            print("Which task do you want to remove from the To-Do List? (Note: use lower case font) ")
            strTask = input("Enter task or type 'exit' to return to main menu: ")
            if strTask.lower() == "exit":
                break
            for row in lstTable:
                if row ["Task"].lower() == strTask.lower():
                    lstTable.remove(row)
                    print("Task has been removed.")
                    print(lstTable, "<< List with Dictionary Objects.")
                    break
            else:
                print("Task not found.")
                print(lstTable, "<< List with Dictionary Objects.")
                strChoice = input("Exit? Yes (y) or No (n): ")
                if strChoice.lower() == "y":
                    break
                elif strChoice.lower() == "n":
                    break
                else:
                    print("Invalid Input.")
                break
        continue

    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open("ToDoList.txt", "w")
        for row in lstTable:
            objFile.write(str(row["Task"]) + "," + str(row["Priority"]) + "\n")
        objFile.close()
        print("Data has been saved.")
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        print("Preparing to exit program.")
        EndProgram = input("\n(Press Enter to exit.)")
        break  # and Exit the program