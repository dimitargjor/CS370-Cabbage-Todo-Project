import ColorSelection, UtilFunctions
from datetime import date, datetime

todoDir = UtilFunctions.getDirectory()

#Instance variables
dateToday = date.today()
todayString = dateToday.strftime("%m/%d/%Y")

dateColumn = "A"
prioColumn = "B"
statColumn = "C"
descColumn = "D"

complete = u'\u2713'
incomplete = u'\u25CB'
overdue = '\u2613'

#######################################
#argAddItem
#######################################   
def argAddItem(listNotes, listPriority, listDate, workbook):

    worksheet = workbook.active

    #instance variables
    currRow = worksheet.max_row + 1

    #Assign To-Do List item description to appropriate variable
    description = listNotes

    #Assign priority to appropriate variable
    priority = listPriority

    #Set first priority letter to upper case
    firstLetter = priority[0]
    firstLetter = firstLetter.upper()
    
    #Set rest of priority to lower case
    restWord = priority[1:]
    restWord = restWord.lower()

    #Assign priority capitalization
    priority = firstLetter + restWord
    
    #Check if valid priority was entered
    if priority not in ("Low", "Medium", "High"):

        while priority not in ("1", "2", "3"):
            ColorSelection.prRed("\nERROR: Input Must Be High, Meduim, or Low.\n")
            ColorSelection.prGreen("Input priority level:")
            ColorSelection.prPurple("1. Low  \n " +
                "2. Medium  \n " +
                "3. High")
            priority = input("\n" + " Your Input: ")

    #Set value to appropriate priority
    if(priority == '1'):
        priority = "Low"
    elif(priority == '2'):
        priority = "Medium"
    elif(priority == '3'):
        priority = "High"

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

    inputDate = datetime.strptime(date, "%m/%d/%Y")
    today = datetime.strptime(todayString, "%m/%d/%Y")

    if(date == "None" or inputDate > today):
        status = incomplete
    else:
        status = overdue

    #Write the todo list item to excel spreadsheet
    worksheet[descColumn + str(currRow)] = description
    worksheet[prioColumn + str(currRow)] = priority
    worksheet[statColumn + str(currRow)] = status
    worksheet[dateColumn + str(currRow)] = date

    #Save the excel document
    workbook.save(todoDir + 'Notes.xlsx')

    print ("\n Item    : " + description + "\n Priority: " + priority + "\n Due Date: " + date)
    ColorSelection.prGreen("Added Successfully.\n")


#######################################
#addItem
#######################################   
def addItem(workbook):

    worksheet = workbook.active

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
    else:
        parsedDate = datetime.strptime(date, "%m/%d/%Y")

    #today's date
    today = datetime.strptime(todayString, "%m/%d/%Y")

    #If input date is after today's date
    if(date == "None" or parsedDate > today):
        status = incomplete

    #if input date is past today's date
    else:
        status = overdue

    #Write the todo list item to excel spreadsheet
    worksheet[descColumn + str(currRow)] = description
    worksheet[statColumn + str(currRow)] = status
    worksheet[prioColumn + str(currRow)] = priority
    worksheet[dateColumn + str(currRow)] = date

    #Save the excel document
    workbook.save(todoDir + 'Notes.xlsx')

    print ("\n Item    : " + description + "\n Priority: " + priority + "\n Due Date: " + date)
    ColorSelection.prGreen("Added Successfully.\n")