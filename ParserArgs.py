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

    args = parser.parse_args()

    if args.Add and args.Priority:
        ListModification.ArgNoteInput(args.Add, args.Priority,args.Date)

    if args.Read:
        ListModification.read()
    
    if args.Menu:

        UtilFunctions.cls()

        ColorSelection.prGreen("Choose a number from the menu options:")
        ColorSelection.prPurple(" 1. Add to Notes \n " +
        " 2. Display All Notes \n " +
        " 3. Display High Priority Notes \n " +
        " 4. Clear Notes \n " +
        "-1. Quit")

        choice = input("  Your Input: ")

        while (choice != '-1'):
            
            if choice == '1':
                ListModification.addNotes() 
            
            elif choice == '2':
                ListModification.read()

            elif choice == '3':
                ListModification.readHigh()
            
            elif choice == '4':
                ListModification.clear()

            else:
                ColorSelection.prRed("ERROR: Invalid Input.\n")
        
            ColorSelection.prGreen("\n" + "Choose a number from the menu options:")
            ColorSelection.prPurple(" 1. Add to Notes \n " +
            " 2. Display All Notes \n " +
            " 3. Display High Priority Notes \n " +
            " 4. Clear Notes \n " +
            "-1. Quit")
            
            choice = input("  Your Input: ")

