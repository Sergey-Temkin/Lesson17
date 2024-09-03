#Package(Folder) , Module(File)

#Importing Add/Print functions from: "dest":Package , Module:"actions"
from dest.actions import add_destination,print_destinations
#Importing Load/Save functions from: "storage":Package , Module:"loadsave"
from storage.loadsave import load,save
#Importing from icecream ic function
from icecream import ic

my_destinations = []

    
def menu():
    load()
    #icecream function:
    ic(my_destinations)
    while True:
        ic("1-Add")
        ic("2-List")
        ic("3-Exit")
        selection = input("Your command? ")
        if selection == "1":
            add_destination(my_destinations)
        if selection == "2":
            print_destinations(my_destinations)
        if selection == "3":
            save()
            exit()
# if __name__ == "__main__": 
# Construct in Python is used to determine whether the current script
# is being run as the main program or if it is being imported as a module into another script.
# This is important for writing code that can be both run as a standalone program and imported as a module into other programs
# When you RUN the program from app.py you get:"__main__" 
# When you RUN the program from other package you get the name of that package            
if __name__ == "__main__":
    print("Package ROOT:", __name__)
    menu()
