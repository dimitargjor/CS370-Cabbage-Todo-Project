import argparse
import ListModification
import ColorSelection
from pickle import TRUE
import UtilFunctions

def userArgs():
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
        ListModification.ArgNoteInput(args.Add, args.Priority,args.Date)

    if args.Read:
        ListModification.read()
    
    if args.Clear:
        ListModification.clear()

    if args.ClearAll:
        ListModification.clearAll()

    if args.Edit:
        ListModification.edit()
    
    if args.Menu:

        UtilFunctions.cls()

        ColorSelection.prGreen(" Choose a number from the menu options:")
        ColorSelection.prPurple(" 1. Add to Notes \n " +
        " 2. Display All Notes \n " +
        " 3. Display High Priority Notes \n " +
        " 4. Edit Item \n " + 
        " 5. Clear Notes \n " +
        "-1. Quit")

        choice = input("\n" + " Your Input: ")

        while (choice != '-1'):
            
            if choice == '1':
                ListModification.addNotes() 
            
            elif choice == '2':
                ListModification.read()

            elif choice == '3':
                ListModification.readHigh()

            elif choice == '4':
                ListModification.edit()
            
            elif choice == '5':
                UtilFunctions.cls()
                ColorSelection.prGreen("What would you like to delete?")
                ColorSelection.prPurple(" 1. A single To-Do List row\n" + "  2. The entire To-Do List\n" + " -1. Quit\n")
                deleteType = input("  Your Input: ")
                
                if(deleteType == '1'):
                    ListModification.clear()
                elif(deleteType == '2'):
                    ListModification.clearAll()
                else:
                    ColorSelection.prRed("\nDeletion Cancelled.\n")

            else:
                ColorSelection.prRed("ERROR: Invalid Input.\n")
        
            ColorSelection.prGreen("\n" + " Choose a number from the menu options:")
            ColorSelection.prPurple(" 1. Add to Notes \n " +
            " 2. Display All Notes \n " +
            " 3. Display High Priority Notes \n " +
            " 4. Edit Item \n " + 
            " 5. Clear Notes \n " +
            "-1. Quit")
            
            choice = input(" Your Input: ")

