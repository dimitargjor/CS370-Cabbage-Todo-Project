import ColorSelection
import UtilFunctions
from os.path import exists

todoDir = UtilFunctions.getDirectory()

#Instance variables
dateColumn = "A"
prioColumn = "B"
descColumn = "C"

workbook = UtilFunctions.getWorkbook()

worksheet = workbook.active

def ArgNoteInput(listNotes, listPriority, listDate):

    #instance variables
    currRow = worksheet.max_row + 1

    #Assign To-Do List item description to appropriate variable
    description = listNotes

    #Assign priority to appropriate variable
    priority = listPriority

    #Check if valid priority was entered

    while priority not in ("Low", "Medium", "High"):
        ColorSelection.prRed("ERROR: Input Must Be High, Meduim, or Low")
        ColorSelection.prCyan("Input the priority level (LOW/MEDIUM/HIGH):")
        priority = input()


    #Assign due date to appropriate variable
    date = listDate

    #Check if entered date is valid
    if(date != None):
        while(not UtilFunctions.checkDate(date)):
            ColorSelection.prRed("ERROR: Date Entered Is Invalid")
            ColorSelection.prCyan("Input a due date (MM/DD/YYYY):")
            date = input()
    else:
        date = "None"

    #Write the todo list item to excel spreadsheet
    worksheet[descColumn + str(currRow)] = description
    worksheet[prioColumn + str(currRow)] = priority
    worksheet[dateColumn + str(currRow)] = date

    #Save the excel document
    workbook.save(todoDir + 'Notes.xlsx')


def read():

    #Clear screen
    UtilFunctions.cls()

    first = True

    #IF Notes file exists
    if (UtilFunctions.checkExistence()):

        spaceString = ""

        #FOR Every row in the list
        for row in worksheet.iter_rows():

            if(not first):
                index = row[0].row - 1 
                print(str(index) + ". ", end="")

            if(first):
                print("   ", end = "")

            #FOR Every cell in the row
            for cell in row:

                #Adjust empty space
                space = 20 - len(str(cell.value))
        
                #FOR all spaces
                for i in range(space):

                    #Add empty space
                    spaceString += " "

                #Print cell value
                print (cell.value, end = spaceString)

                spaceString = ""
            print("")

            if first == True:
                print("")
                first = False
    else:
        ColorSelection.prRed("ERROR: File Does Not Exist, You Do Not Have A To-Do List")

def readHigh():

    UtilFunctions.cls()

    if (exists(todoDir + 'Notes.xlsx')):
        spaceString = ""

        header = ""
        for row in worksheet[1]:
            header += row.value
            header += "            "

        print(header + "\n")

        for row in worksheet.iter_rows():

            if row[1].value == 'High':
                for cell in row:
                    space = 20 - len(str(cell.value))
                    for i in range(space):
                        spaceString += " "
                    print (cell.value, end = spaceString)
                    
                    spaceString = ""
                print("")

    else:
        ColorSelection.prRed("ERROR: File Does Not Exist, You Do Not Have A To-Do List")

def clear():

    UtilFunctions.cls()

    if (UtilFunctions.checkExistence()):

        read()

        ColorSelection.prGreen("\nSelect row item to be deleted.")
        selection = input("Your Input: ")
        selection = int(selection)
        maxRow = worksheet.max_row - 1

        if (selection <= maxRow and selection > 0):

            UtilFunctions.cls()
            selection = selection + 1

            header = ""
            spaceString = ""
            for row in worksheet[1]:
                header += row.value
                header += "            "

            print(header + "\n")

            for cell in worksheet[selection]:

                space = 20 - len(str(cell.value))
                for i in range(space):
                    spaceString += " "
                print (cell.value, end = spaceString)

                spaceString = ""
            print("")

            ColorSelection.prGreen("\nAre you sure you want to delete this row? (Y / Any other key)")
            answer = input("Your Input: ")
            answer = answer.lower()
            if(answer == "y"):

                worksheet.delete_rows(selection)

                workbook.save(todoDir + 'Notes.xlsx')

                ColorSelection.prCyan("\nRow deleted successfully.")
            else:
                ColorSelection.prRed("\nCancelled row deletion.")
        else:
            ColorSelection.prRed("\nInvalid row selected. Deletion cancelled.\n")

    else:
        ColorSelection.prRed("\nERROR: File does not exist, you do not have a To-Do List.")

def clearAll():
    UtilFunctions.cls()
    ColorSelection.prRed("WARNING: Are you sure you want to clear all of your To-Do List items? (Y / Any other key)")
    choice = input(" Your Input: ")
    choice = choice.lower()
    if choice == 'y':
        worksheet.delete_rows(2, worksheet.max_row)

        workbook.save(todoDir + 'Notes.xlsx')

        ColorSelection.prCyan("\nTo-Do List cleared.\n")
    else:
        ColorSelection.prRed("\nFile deletion cancelled.\n")


def edit():

    UtilFunctions.cls()

    if (UtilFunctions.checkExistence()):

        maxRow = worksheet.max_row

        read()

        ColorSelection.prGreen("\nWhich To-Do List Item would you like to edit?")
        selection = input("Your Input: ")
        selection = int(selection)

        selection = selection + 1

        if (selection <= maxRow and selection > 1):

            UtilFunctions.cls()

            spaceString = ""
            for cell in worksheet[selection]:

                space = 20 - len(str(cell.value))
                for i in range(space):
                    spaceString += " "
                print (cell.value, end = spaceString)

                spaceString = ""
            print("")

            ColorSelection.prPurple("\nWhich attribute would you like to update?")
            ColorSelection.prGreen("1. Description \n" + 
                                   " 2. Priority \n" + 
                                   " 3. Due Date \n")

            editType = input("Your Input: ")

            if(editType == '1'):
                UtilFunctions.cls()
                ColorSelection.prGreen("What would you like to change the description to? (-1 to Quit)")
                newDesc = input("Your Input: ")

                if(newDesc != '-1'):
                    worksheet[descColumn + str(selection)] = newDesc
                    ColorSelection.prCyan("\nItem edited successfully.\n")
                    workbook.save(todoDir + 'Notes.xlsx') 
                else:
                    ColorSelection.prRed("\nItem edit cancelled.\n")
            
            elif(editType == '2'):

                UtilFunctions.cls()
                #Input priority level
                ColorSelection.prGreen("Input priority level:")
                ColorSelection.prPurple(" 1. Low  \n " +
                    " 2. Medium  \n " +
                    " 3. High \n " + 
                    "-1. Quit")
                priority = input("\n" + " Your Input: ")

                if priority == "1":
                    worksheet[prioColumn + str(selection)] = "Low"
                    workbook.save(todoDir + 'Notes.xlsx')
                    ColorSelection.prCyan("\nPriority successfully changed.\n")

                elif priority == "2":
                    worksheet[prioColumn + str(selection)] = "Medium"
                    workbook.save(todoDir + 'Notes.xlsx')
                    ColorSelection.prCyan("\nPriority successfully changed.\n")

                elif priority == "3":
                    worksheet[prioColumn + str(selection)] = "High"
                    workbook.save(todoDir + 'Notes.xlsx')
                    ColorSelection.prCyan("\nPriority successfully changed.\n")

                else:
                    ColorSelection.prRed("\nPriority change cancelled.\n")

            elif(editType == "3"):

                UtilFunctions.cls()
                ColorSelection.prGreen("What will the new Due Date be? (MM/DD/YYYY)")
                date = input()
                if(UtilFunctions.checkDate(date)):

                        worksheet[dateColumn + str(selection)] = date
                        workbook.save(todoDir + 'Notes.xlsx')
                        ColorSelection.prCyan("\nDate successfully changed.\n")

                else:
                    ColorSelection.prRed("\nInvalid date entered. File edit cancelled.\n")
            else:
                ColorSelection.prRed("\nInvalid edit type. File edit cancelled.\n")

            workbook.save(todoDir + 'Notes.xlsx')

        else:
            ColorSelection.prRed("\nInvalid row selected. File edit cancelled.\n")

    else:
        ColorSelection.prRed("\nERROR: File does not exist, you do not have a To-Do List\n")


def addNotes():

    #instance variables
    currRow = worksheet.max_row + 1

    UtilFunctions.cls()
    
    #Input todo list item description
    ColorSelection.prGreen("Input the description of the To-Do List item.")
    description = input(" Your Input: ")

    UtilFunctions.cls()

    #Input priority level
    ColorSelection.prGreen("Input priority level:")
    ColorSelection.prPurple("1. Low  \n " +
        "2. Medium  \n " +
        "3. High")
    priority = input("\n" + " Your Input: ")

    #Check if valid priority was entered
    while priority not in ("1", "2", "3"):
        ColorSelection.prRed("\nERROR: Input Must Be High, Meduim, or Low.\n")
        ColorSelection.prGreen("Input priority level:")
        ColorSelection.prPurple("1. Low  \n " +
            "2. Medium  \n " +
            "3. High")
        priority = input("\n" + " Your Input: ")

    if(priority == '1'):
        priority = "Low"
    elif(priority == '2'):
        priority = "Medium"
    elif(priority == '3'):
        priority = "High"

    UtilFunctions.cls()
    
    #Input due date
    ColorSelection.prGreen("Input a due date (MM/DD/YYYY) or '-1' to skip.")
    date = input(" Your Input: ")

    #Check if entered date is valid

    while(date != '-1' and not UtilFunctions.checkDate(date)):

        ColorSelection.prRed("\nERROR: Date Entered Is Invalid\n")
        ColorSelection.prGreen("Input a due date (MM/DD/YYYY) or '-1' to skip.")
        date = input(" Your Input: ")


    if(date == '-1'):
        date = "None"

    #Write the todo list item to excel spreadsheet
    worksheet[descColumn + str(currRow)] = description
    worksheet[prioColumn + str(currRow)] = priority
    worksheet[dateColumn + str(currRow)] = date

    #Save the excel document
    workbook.save(todoDir + 'Notes.xlsx')