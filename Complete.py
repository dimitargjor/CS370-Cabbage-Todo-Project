import Read, ColorSelection, UtilFunctions

def markComplete(workbook):
    
    Read.read(workbook)
        
    complete = u'\u2713'
    incomplete = u'\u25CB'
    overdue = '\u2613'
    overdueComplete = u'\u2713' + u'\u00D7'
    statColumn = "C"

    worksheet = workbook.active

    todoDir = UtilFunctions.getDirectory()

    maxRow = worksheet.max_row

    ColorSelection.prGreen("\nWhich To-Do List Item would you like mark as complete?")
    selection = input("Your Input: ")
    selection = int(selection)

    selection = selection + 1

    if (selection <= maxRow and selection > 1):

        UtilFunctions.cls()

        if(worksheet[statColumn + str(selection)].value == overdue):

            worksheet[statColumn + str(selection)]  = overdueComplete

            workbook.save(todoDir + 'Notes.xlsx')

            ColorSelection.prCyan("\nItem marked as Completed.\n")

        elif(worksheet[statColumn + str(selection)].value == incomplete):

            worksheet[statColumn + str(selection)]  = complete

            workbook.save(todoDir + 'Notes.xlsx')

            ColorSelection.prCyan("\nItem marked as Completed.\n")

        else:

            ColorSelection.prCyan("\nItem is already Completed.\n")

    else:
         ColorSelection.prRed("\nInvalid row selected.\n")
