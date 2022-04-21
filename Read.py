import ColorSelection, UtilFunctions


def read(workbook):
    
    worksheet = workbook.active

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

                if (index < 10): 
                    print(" " + str(index) + ". ", end="")
                else:
                    print(str(index) + ". ", end="")

            if(first):
                print("    ", end = "")

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


def readHigh(workbook):

    worksheet = workbook.active

    UtilFunctions.cls()

    if (UtilFunctions.checkExistence()):
        spaceString = ""

        header = "    "
        for row in worksheet[1]:
            header += row.value

            if(len(str(row.value)) < 8):
                space = 8 - len(str(row.value))
                for i in range(space):
                    header += " "

            header += "            "

        print(header + "\n")

        for row in worksheet.iter_rows():

            if row[1].value == 'High':

                index = row[0].row - 1

                if (index < 10): 
                    print(" " + str(index) + ". ", end="")
                else:
                    print(str(index) + ". ", end="")

                for cell in row:
                    space = 20 - len(str(cell.value))
                    for i in range(space):
                        spaceString += " "
                    print (cell.value, end = spaceString)
                    
                    spaceString = ""
                print("")

    else:
        ColorSelection.prRed("ERROR: File Does Not Exist, You Do Not Have A To-Do List")