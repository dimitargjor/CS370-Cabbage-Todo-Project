import sys
def FileSystem():
    import os 
    from PrintColors import PrintColor
    from os.path import expanduser
    import sys

    if sys.platform != 'win32':
        doccumentsDir = '/var'
        

    #Find user home directory
    homeDir = expanduser("~")

    #Join home directory path to Doccuments
    Doccuments = os.path.join(homeDir, "Doccuments\\")

    #IF the ToDo List directory doesn't exist
    if os.path.isdir(Doccuments + "ToDo List\\") == False:
        os.mkdir(Doccuments + "ToDo List\\")
        print("NOTICE:")
        PrintColor.prRed("directory Created")
        #Make ToDo List directory

    #Make variable with ToDo List directory
    TodoDir = os.path.join(Doccuments, "ToDo List\\")

    #Return ToDo List directory
    return TodoDir

print(sys.platform)