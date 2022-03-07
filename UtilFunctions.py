import os 
from os.path import expanduser
from openpyxl import Workbook, load_workbook
from os.path import exists
from openpyxl.styles import Font
import datetime


#Returns path to ToDo List directory, and creates it if it doesn't exist
def getDirectory():    
    import os 
    import ColorSelection
    from os.path import expanduser
    import sys

    var = sys.platform

    if (var != 'win32'):
        DocList = '/var'
        if os.path.isdir(DocList + "ToDo List\\") == False:
            os.mkdir(DocList + "ToDo List\\")
            print("NOTICE:")
            ColorSelection.prRed("directory Created")
        TodoDir = os.path.join(DocList, "ToDo List\\")


    else:

        #Find user home directory
        homeDir = expanduser("~")

        #Join home directory path to Doccuments
        Doccuments = os.path.join(homeDir, "Documents\\")

        #IF the ToDo List directory doesn't exist
        if os.path.isdir(Doccuments + "ToDo List\\") == False:
            os.mkdir(Doccuments + "ToDo List\\")
            print("NOTICE:")
            ColorSelection.prRed("directory Created")
            #Make ToDo List directory

        #Make variable with ToDo List directory
        TodoDir = os.path.join(Doccuments, "ToDo List\\")

        #Return ToDo List directory
    return TodoDir

#Returns workbook for writing in excel file. Creates a new worksheet if it doesn't exist
def getWorkbook():

    todoDir = getDirectory()

    #Instance variables
    descColumn = "A"
    prioColumn = "B"
    dateColumn = "C"

    if(exists(todoDir + 'Notes.xlsx')):
        workbook = load_workbook(todoDir + 'Notes.xlsx')
        worksheet =  workbook.active

    else:

        #Create a new workbook
        workbook = Workbook()
        worksheet =  workbook.active
        worksheet.title = "ToDo List"

        #Set column length
        worksheet.column_dimensions[descColumn].width = 20
        worksheet.column_dimensions[prioColumn].width = 15
        worksheet.column_dimensions[dateColumn].width = 15

        #Set headings style
        worksheet[descColumn + "1"].font = Font(color = "00800080", bold = True)
        worksheet[prioColumn + "1"].font = Font(color = "00800080", bold = True) 
        worksheet[dateColumn + "1"].font = Font(color = "00800080", bold = True) 

        #Set column headings
        worksheet[descColumn + "1"] = "Description"
        worksheet[prioColumn + "1"] = "Priority"
        worksheet[dateColumn + "1"] = "Due Date"

        workbook.save(todoDir + 'Notes.xlsx')

    return workbook

def checkExistence():

    todoDir = getDirectory()
    
    output = False

    if(exists(todoDir + 'Notes.xlsx')):
        output = True

    return output


#Function that checks if a valid date was entered
def checkDate(dateInput):

    output = True

    try:
        month, day, year = dateInput.split('/')
        try:
            datetime.datetime(int(year), int(month), int(day))
        except ValueError:
            output = False
    except ValueError:
        output = False

    return output


def cls():  
    os.system('cls' if os.name == 'nt' else 'clear')
