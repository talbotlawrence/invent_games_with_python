import random
import time

def displayIntro():
    print("You are in a land full of Aardvarks.  In front of you,")
    print("you see two caves.  In one cave, the Aardvark is friendly")
    print("and will share his treasure with you.  The other Aardvark")
    print("is greedy and hungry, and will eat you on sight.")
    print()

def chooseCave():
    cave = ""
    while cave != "1" and cave != "2":
        cave = input("Which cave will you go into? (1 or 2)")

    return cave

#chosenCave in the checkCave method below could be potato
def checkCave(potato):
    print("You approach the cave...")
    time.sleep(2)
    print("It is dark and spooky...")
    time.sleep(2)
    print("A large Aardvark jumps out in front of you!!  He opens his jaws and...")
    print("")
    time.sleep(2)

    friendlyCave = random.randint(1,2)

    if potato == str(friendlyCave):
        print("Yay, you just got some treasure fool!!")
    else:
        print("Well, you just got eaten!!  Sorry bro!")


#Below kicks off the whole game
#None of the methods get called until the lines below
playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)       #caveNumber will be the value of 'cave' from the checkCave method
    playAgain = input("Do you want to play again? (yes or no)")