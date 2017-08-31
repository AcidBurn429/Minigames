import random
from pathlib import Path

file = Path("number_gussing_highscorelist.txt")
if file.exists() == False:
    datei = open("number_gussing_highscorelist.txt", "w")
    datei.write("")
    datei.close()


def checkHighscore(tryes):
    try:
        file = open("number_gussing_highscorelist.txt", "a")

        username = input("Username: ")

        file.write(username + "::" + str(tryes))

        file.close()
    except IOError:
        print("Error: File not found!")

def guss_number(start, ende):
    number = random.randint(int(start), int(ende))

    check = False
    tryes = 1
    while check != True:
        inp = input("Your guss: ")

        inp = int(inp)

        hallo = True
        try:
            test1 = int(start)
            test2 = int(ende)
        except ValueError:
            print("The numbers must be valid integer values")
            hallo = False

        if inp > number:
            print("Your number is too big!")
        if inp < number:
            print("Your number is too low!")
        if inp == number:
            print("Your guss is correct!")
            print("The secret number is " + str(number))
            print("You needed " + str(tryes) + " tries for finding the number!")
            quest = input("Do you want to stand on the highscore list?[y/n] ")
            if quest == "y":
                checkHighscore(tryes)
            check = True
        tryes = tryes + 1

def help():
    print("number gussing")
    print("Choose a level!")
    print("1        : numbers from 1 to 10")
    print("2        : numbers from 1 to 100")
    print("3        : numbers from 1 to 1000")
    print("x        : choose your own range")
    print("writer   : shows the creater of this programm")
    print("highscore: shows the highscore list")
    print("help     : shows this message")
    print("exit     : close the programm")

help()

while True:
    inp = input("> ")

    if inp == "1":
        guss_number(1,10)
    elif inp == "2":
        guss_number(1,100)
    elif inp == "3":
        guss_number(1,1000)
    elif inp == "x":
        check = False
        while check != True:
            start = input("start: ")
            ende =  input("end  : " )

            if start > ende:
                print("The start value must be lower than the end value")
            if start == ende:
                print("The start and the end value must be diffrent")
            hallo = True
            try:
                test1 = int(start)
                test2 = int(ende)
            except ValueError:
                print("The numbers must be valid integer values")
                hallo = False
            if start < ende and start != ende and hallo == True:
                check = True
                guss_number(start, ende)

    elif inp == "writer":
        print("The programm was created by AcidBurn429 (GitHub name)")
    elif inp == "highscore":
        try:
            file = open("number_gussing_highscorelist.txt", "r")
            print("Usernames Scores")
            for line in file.readlines():
                content = line.split("::",1)
                print(content[0] + " " + content[1])
            file.close()
        except IOError:
            print("Error: File not found!")
    elif inp == "help":
        help()
    elif inp == "exit":
        break
    else:
        print("Sorry, but this is no instruction! Look here:")
        help()
