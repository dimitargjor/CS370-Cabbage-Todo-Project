import ColorSelection, UtilFunctions
import Read

todoDir = UtilFunctions.getDirectory()

#Instance variables
dateColumn = "A"
prioColumn = "B"
descColumn = "C"

def edit(workbook):

    worksheet = workbook.active

    UtilFunctions.cls()

    if (UtilFunctions.checkExistence()):

        maxRow = worksheet.max_row

        Read.read(workbook)

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