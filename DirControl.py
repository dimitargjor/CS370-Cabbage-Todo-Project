def FileSystem():
    import os 
    from os.path import expanduser

    #Find user home directory
    homeDir = expanduser("~")

    #Join home directory path to desktop
    desktop = os.path.join(homeDir, "Desktop\\")

    #IF the ToDo List directory doesn't exist
    if os.path.isdir(desktop + "ToDo List\\") == False:

        #Make ToDo List directory
        os.mkdir(desktop + "ToDo List\\")

    #Make variable with ToDo List directory
    TodoDir = os.path.join(desktop, "ToDo List\\")
    
    #Return ToDo List directory
    return TodoDir