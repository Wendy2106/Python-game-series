import time
shipName = "Conquer"
captain = "Emnie"
location = "Earth"
destination = "Earth"
password = "You are the best"

def universeMap():
    print("--(Sun)---------------------------------------------")
    print("-----(Mercury)--------------------------------------")
    print("---------(Venus)------------------------------------")
    print("--------------(Earth)-------------------------------")
    print("-------------------(Mars)---------------------------")
    print("-----------------------(Jupiter)--------------------")
    print("----------------------------(Saturn)----------------")
    print("---------------------------------(Uranus)-----------")
    print("-------------------------------------(Neptune)------")
    print("------------------------------------------(Pluto)---")

def spacecraft(): 
    print("  o                |")
    print("            .     -O-")
    print(" .                 |        *      .     -0-")
    print("        *  o     .    '       *      .        o")
    print("               .         .        |      *")
    print("    *             *              -O-          .")
    print("          .             *         |     ,")
    print("                 .           o")
    print("         .---.")
    print("   =   _/__~0_\_     .  *            o       '")
    print("  = = (_________)             .")
    print("                  .                        *")
    print("        *               - ) -       *")


for i in range(5):
    pAttempt = input("Enter the password: ")
    if(pAttempt == password):
        break
    else:
        print("Password is incorrect")
if (pAttempt != password):
    print("You've entered your password incorrectly 5 times")
    print("The spacecraft will be disabled 24 hours.")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("See you tomorrow! -v-")
else:
    spacecraft()
    print("Password is correct. Welcome to the " + shipName)
    print("")
    print("The spaceship " + shipName + "is currently visiting " + location + ".")
    choice = ""
    while choice != "/exit":
        print("")
        time.sleep(1)
        print("What would you like to do, " + captain + "?")
        print("a. Travel to another planet")
        print("b. Go explore")
        print("c. Open the navigation system")
        print("d. Teleport to Earth")
        print("/exit to exit")
        print("")
        choice = input("Enter your choice: ")
        if choice == "a":
            universeMap()
            destination = input("Where would you like to go? ")
            print("Leaving " + location)
            if(destination == "Sun"):
                print("Activating the fire protection system")
                time.sleep(1)
            print("Traveling to " + destination + ", please waiting...")
            time.sleep(1)
            print("|")
            time.sleep(1)
            print("|")
            time.sleep(1)
            print("|")
            time.sleep(1)
            print("|")
            time.sleep(1)
            print("|")
            print("v")
            print("Arrived at " + destination)
            location = destination
        elif choice == "b":
            print("Choose a discovery method:")
            print("1. Use the radar")
            print("2. Go on your own")
            exploreChoice = input("Enter your choice(1/2):")
            if exploreChoice =="1":
                print("Automatic radar mode is enabled to detect life or resources present on this planet.")
            elif exploreChoice =="2":
                check = input("Check that you have brought all necessary equipment, especially spare oxygen cylinders? (y/n)")
                while(check != "y"):
                    print("Please check again, otherwise you may be in danger.")
                    check = input("Check that you have brought all necessary equipment, especially spare oxygen cylinders? (y/n)")
                print("Wish you discover something interesting!")
            else:
                print("Invalid input. Please select 1 or 2")   
        elif choice == "c":
            print("The navigation system opened")
            time.sleep(1)
            a,b = input("Select coordinate (X , Y):").split(",")
            print("Moving to coordinate (" + a  + " , " + b + ")")
            time.sleep(3)
            print("Arrived")
        elif choice == "d":
            confirm = input("Are you sure you want to teleport to Earth? (y/n)")
            if confirm == "y":
                print("Ship will teleport to Earth after 1s")
                print("Goodbye " + destination)
                print("BOOM")
                time.sleep(1)
                print("Welcome back to Earth. You've worked hard!")
                choice = "/exit"
        elif choice == "/exit":
                print("Goodbye")
        else:
                print("Invalid input. Please select a, b, c or d. /exit to exit")


