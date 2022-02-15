import argparse
import CommandFunctions
from PrintColors import PrintColor
from pickle import TRUE
from TerminalControls import Clear


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
    CommandFunctions.ArgNoteInput(args.Add, args.Priority,args.Date)

if args.Read:
    CommandFunctions.read()
 
if args.Menu:

    Clear.cls()

    PrintColor.prGreen("Choose a number from the menu options:")
    PrintColor.prPurple(" 1. Add to Notes \n " +
    " 2. Display All Notes \n " +
    " 3. Display High Priority Notes \n " +
    " 4. Clear Notes \n " +
    "-1. Quit")

    choice = input("  Your Input: ")

    while (choice != '-1'):
        
        if choice == '1':
           CommandFunctions.addNotes() 
        
        elif choice == '2':
            CommandFunctions.read()

        elif choice == '3':
            CommandFunctions.readHigh()
        
        elif choice == '4':
            CommandFunctions.clear()

        else:
            PrintColor.prRed("ERROR: Invalid Input.\n")
    
        PrintColor.prGreen("\n" + "Choose a number from the menu options:")
        PrintColor.prPurple(" 1. Add to Notes \n " +
        " 2. Display All Notes \n " +
        " 3. Display High Priority Notes \n " +
        " 4. Clear Notes \n " +
        "-1. Quit")
        
        choice = input("  Your Input: ")

