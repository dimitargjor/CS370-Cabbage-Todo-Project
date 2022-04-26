import argparse
import ColorSelection
import UtilFunctions
import Clear, Edit, Read, Add, Complete

workbook = UtilFunctions.getWorkbook()

def todoFunc():

    UtilFunctions.checkCurrDate(workbook)

    msg= """this progam is designed as a utility tool too keep you on track of your tasks
            For quick input use the following shortcuts on the commandline"""

    parser= argparse.ArgumentParser(description = msg)

    parser.add_argument("-a", "--Add", help = "Add item to list")
    parser.add_argument("-p", "--Priority", help = "this will give a priority to the item you would like to add")
    parser.add_argument("-d", "--Date", help = "This will add a due date to your list")
    parser.add_argument("-r", "--Read", help = "This will print your to-do list to the terminal", action="store_true")
    parser.add_argument("-m", "--Menu", help = "This will open an interactive menu for input", action="store_true")
    parser.add_argument("-c", "--Clear", help = "This will open prompt to delete one item from list", action="store_true")
    parser.add_argument("-ca", "--ClearAll", help = "This will open clear the entire To-Do list", action="store_true")
    parser.add_argument("-e", "--Edit", help = "This will open prompt to edit a item's attribute", action="store_true")

    args = parser.parse_args()

    if args.Add and args.Priority:
        Add.argAddItem(args.Add, args.Priority, args.Date, workbook)

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

