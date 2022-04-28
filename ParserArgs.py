import argparse
import ColorSelection
import UtilFunctions
import Clear, Edit, Read, Add, Complete

workbook = UtilFunctions.getWorkbook()

def todoFunc():

    UtilFunctions.checkCurrDate(workbook)

    msg= "A command-line based utility tool geared towards software developers, allowing a user to configure a To-Do list of items."

    parser= argparse.ArgumentParser(description = msg)

    parser.add_argument("-add", "--Add", help = "Add item to list.")
    parser.add_argument("-p", "--Priority", help = "Specify item priority (Low/Medium/High).")
    parser.add_argument("-c", "--Category", help = "Specify what developer category item belongs to.")
    parser.add_argument("-d", "--Date", help = "Add due date for item in format mm/dd/yyyy.")
    parser.add_argument("-r", "--Read", help = "Display the full To-Do list.", action="store_true")
    parser.add_argument("-m", "--Menu", help = "Open interactive menu with all modification features included.", action="store_true")
    parser.add_argument("-cl", "--Clear", help = "Open prompt to delete a single item in the list.", action="store_true")
    parser.add_argument("-cla", "--ClearAll", help = "Open prompt to delete the entire To-Do list", action="store_true")
    parser.add_argument("-e", "--Edit", help = "Open prompt to edit a specific item in the list. ", action="store_true")

    args = parser.parse_args()

    if args.Add:
        Add.argAddItem(args.Add, args.Priority, args.Category, args.Date, workbook)

    if args.Read:
        Read.read(workbook)

    if args.Clear:
        Clear.clear(workbook)

    if args.ClearAll:
        Clear.clearAll(workbook)

    if args.Edit:
        Edit.edit(workbook)
    
    if args.Menu:

        UtilFunctions.cls()

        ColorSelection.prGreen("Choose a number from the menu options:")
        ColorSelection.prPurple(" 1. Add an Item. \n " +
        " 2. Mark Completed Item/s. \n " + 
        " 3. Delete Item/s. \n " +
        " 4. Edit Item. \n " + 
        " 5. Display All Items. \n " +
        " 6. Display High Priority Items. \n " +
        "-1. Quit.")

        choice = input("\n" + " Your Input: ")

        while (choice != '-1'):
            
            if choice == '1':
                Add.addItem(workbook) 

            elif choice == '2':
                Complete.markComplete(workbook)

            elif choice == '3':
                UtilFunctions.cls()
                ColorSelection.prGreen("What would you like to delete?")
                ColorSelection.prPurple(" 1. A singular item.\n" + "  2. The entire list.\n" + " -1. Quit.\n")
                deleteType = input("  Your Input: ")

                if(deleteType == '1'):
                    Clear.clear(workbook)
                elif(deleteType == '2'):
                    Clear.clearAll(workbook)
                else:
                    ColorSelection.prRed("\nDeletion Cancelled.\n")
 
            elif choice == '4':
                Edit.edit(workbook)               
            
            elif choice == '5':
                Read.read(workbook)

            elif choice == '6':
                Read.readHigh(workbook) 

            else:
                ColorSelection.prRed("ERROR: Invalid Input.\n")
            
            ColorSelection.prGreen("Choose a number from the menu options:")
            ColorSelection.prPurple(" 1. Add an Item. \n " +
            " 2. Mark Completed Item/s. \n " + 
            " 3. Delete Item/s. \n " +
            " 4. Edit Item. \n " + 
            " 5. Display All Items. \n " +
            " 6. Display High Priority Items. \n " +
            "-1. Quit.")
            
            choice = input(" Your Input: ")

