import ColorSelection, UtilFunctions
import Read

todoDir = UtilFunctions.getDirectory()

def clear(workbook):

    worksheet = workbook.active

    UtilFunctions.cls()

    if (UtilFunctions.checkExistence()):

        Read.read(workbook)

        ColorSelection.prGreen("\nSelect row item to be deleted.")
        selection = input("Your Input: ")
        selection = int(selection)
        maxRow = worksheet.max_row - 1

        if (selection <= maxRow and selection > 0):

            UtilFunctions.cls()
            selection = selection + 1

            header = ""
            spaceString = ""
            for cell in worksheet[1]:

                #CHANGE LATER
                if(cell.value == 'Status'):
                    header += cell.value
                    header += "              "                            
                else:
                    header += cell.value
                    header += "            "

            print(header + "\n")

            for cell in worksheet[selection]:

                space = 20 - len(str(cell.value))
                for i in range(space):
                    spaceString += " "
                print (cell.value, end = spaceString)

                spaceString = ""
            print("")

            ColorSelection.prGreen("\nAre you sure you want to delete this row? (Y / N)")
            answer = input("Your Input: ")
            answer = answer.lower()
            if(answer == "y"):

                worksheet.delete_rows(selection)

                workbook.save(todoDir + 'Notes.xlsx')

                ColorSelection.prCyan("\nRow deleted successfully.\n")
            else:
                ColorSelection.prRed("\nCancelled row deletion.")
        else:
            ColorSelection.prRed("\nInvalid row selected. Deletion cancelled.\n")

    else:
        ColorSelection.prRed("\nERROR: File does not exist, you do not have a To-Do List.")

def clearAll(workbook):

    worksheet = workbook.active

    UtilFunctions.cls()
    ColorSelection.prRed("WARNING: Are you sure you want to clear all of your To-Do List items? (Y / N)")
    choice = input(" Your Input: ")
    choice = choice.lower()
    if choice == 'y':
        worksheet.delete_rows(2, worksheet.max_row)

        workbook.save(todoDir + 'Notes.xlsx')

        ColorSelection.prCyan("\nTo-Do List cleared.\n")
    else:
        ColorSelection.prRed("\nFile deletion cancelled.\n")