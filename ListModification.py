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
    ColorSelection.prRed("***WARNING***")
    ColorSelection.prGreen("Are you sure you want to clear your To-Do List?")
    ColorSelection.prGreen("To clear list, type 'CONFIRM'. Type any other key to cancel:")
    choice = input(" Your Input: ")
    choice = choice.lower()
    if (choice == "confirm"):
        UtilFunctions.cls()
        worksheet.delete_rows(2, worksheet.max_row+1)

        workbook.save(todoDir + 'Notes.xlsx')
        UtilFunctions.cls()
        ColorSelection.prPurple("You have cleared your file.")

    else:
        UtilFunctions.cls()
        ColorSelection.prPurple("File clear has been cancelled.")

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

