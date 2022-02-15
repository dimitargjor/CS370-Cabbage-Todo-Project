class Clear:
    def cls():  
        import os
        os.system('cls' if os.name == 'nt' else 'clear')