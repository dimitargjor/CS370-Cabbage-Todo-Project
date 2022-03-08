import ColorSelection
import UtilFunctions
from os.path import exists

todoDir = UtilFunctions.getDirectory()

#Instance variables
descColumn = "A"
prioColumn = "B"
dateColumn = "C"

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
    priority = priority.lower()
    while priority not in ("low", "medium", "high"):
        ColorSelection.prRed("ERROR: Input Must Be High, Meduim, or Low")
        ColorSelection.prCyan("Input the priority level (LOW/MEDIUM/HIGH):")
        priority = input()
        priority = priority.lower()

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
    UtilFunctions.cls()
    first = True
    if (UtilFunctions.checkExistence()):
        spaceString = ""
        for row in worksheet.iter_rows():
            for cell in row:
                space = 25 - len(str(cell.value))
        
                for i in range(space):
                    spaceString += " "

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

        print("Description              Priority                 Due Date" + "\n")

        for row in worksheet.iter_rows():

            if row[1].value == 'High':
                for cell in row:
                    space = 25 - len(str(cell.value))
                    for i in range(space):
                        spaceString += " "
                    print (cell.value, end = spaceString)
                    
                    spaceString = ""
                print("")
    else:
        ColorSelection.prRed("ERROR: File Does Not Exist, You Do Not Have A To-Do List")

def clear():
    UtilFunctions.cls()

    ColorSelection.prCyan("What do you want to clear?\n" +
        "1. A single To-Do List item\n" + "2. The entire To-Do List\n")
    ColorSelection.prGreen("Answer with 1 or 2.")
    deleteType = input()

    #wipe one item
    if(deleteType == "1"):
        UtilFunctions.cls()
        if (UtilFunctions.checkExistence()):
            rowNumber = 0
            for row in worksheet.iter_rows():
                print(rowNumber, end=". ")
                for cell in row:
                    print(cell.value, end="|")
                print("")
                rowNumber = rowNumber + 1
            ColorSelection.prCyan("Select To-Do List item to be deleted.")
            selection = input()
            selection = int(selection)
            if (selection < rowNumber and selection > 0):
                UtilFunctions.cls()
                selection = selection + 1
                print("|", end="")
                for cell in worksheet[selection]:
                    print(cell.value, end="|")
                print("")
                ColorSelection.prRed("If this row is deleted, it cannot be recovered.")
                ColorSelection.prCyan("Is this the row you want to delete?")
                ColorSelection.prCyan("Y/N")
                answer = input()
                if(answer == "y" or answer == "Y"):
                    worksheet[descColumn + str(selection)] = ""
                    worksheet[prioColumn + str(selection)] = ""
                    worksheet[dateColumn + str(selection)] = ""
                    workbook.save(todoDir + 'Notes.xlsx')
                    ColorSelection.prCyan("Row clear successful.")
                elif(answer == "n" or answer == "N"):
                    ColorSelection.prPurple("Row clear has been cancelled.")
                else:
                    ColorSelection.prPurple("Invalid answer. Row clear has been cancelled.")

            else:
                ColorSelection.prPurple("Invalid row selection. Row clear has been cancelled.")

        else:
            ColorSelection.prRed("ERROR: File Does Not Exist, You Do Not Have A To-Do List")

def addNotes():

    #instance variables
    currRow = worksheet.max_row + 1

    UtilFunctions.cls()
    
    #Input todo list item description
    ColorSelection.prCyan("Input the description of the To-Do List item:")
    description = input(" Your Input: ")

    UtilFunctions.cls()

    #Input priority level
    ColorSelection.prCyan("Input priority level:")
    ColorSelection.prYellow("1. Low  \n " +
        "2. Medium  \n " +
        "3. High")
    priority = input(" Your Input: ")

    #Check if valid priority was entered
    while priority not in ("1", "2", "3"):
        ColorSelection.prRed("ERROR: Input Must Be High, Meduim, or Low")
        ColorSelection.prCyan("Input priority level:")
        ColorSelection.prYellow("1. Low  \n " +
            "2. Medium  \n " +
            "3. High")
        priority = input(" Your Input: ")

    if(priority == '1'):
        priority = "Low"
    elif(priority == '2'):
        priority = "Medium"
    elif(priority == '3'):
        priority = "High"

    UtilFunctions.cls()
    
    #Input due date
    ColorSelection.prCyan("Input a due date (MM/DD/YYYY) or '-1' to skip:")
    date = input(" Your Input: ")

    #Check if entered date is valid
    if(date != '-1'):
        while(not UtilFunctions.checkDate(date)):
            ColorSelection.prRed("ERROR: Date Entered Is Invalid")
            ColorSelection.prCyan("Input a due date (MM/DD/YYYY):")
            date = input(" Your Input: ")
    else:
        date = "None"
    #Write the todo list item to excel spreadsheet
    worksheet[descColumn + str(currRow)] = description
    worksheet[prioColumn + str(currRow)] = priority
    worksheet[dateColumn + str(currRow)] = date

    #Save the excel document
    workbook.save(todoDir + 'Notes.xlsx')