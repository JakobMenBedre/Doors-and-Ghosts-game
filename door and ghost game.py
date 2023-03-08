import random
import sys
import time

DOOR1=0
DOOR2=0
ghostdoor=0
chosen=0
gameover = False
score =0


start = input("please input G: ")

while gameover == False:
    if start == "g":
        ghostdoor = random.randint(1, 3)
    else:
        sys.exit()

    if ghostdoor == 1:
        DOOR1=2
        DOOR2=3
    elif ghostdoor == 2:
        DOOR2=3
        DOOR1=1
    elif ghostdoor == 3:
        DOOR1=1
        DOOR2=2

    chosen = int(input("input 1, 2 or 3 to chose a door."))
    if chosen == ghostdoor:
        print ("Game Over")
        print("your score was:", score)
        time.sleep(5)
        gameover=True
    elif chosen == DOOR1:
        print("You live!")
        score = score +1 
        print(score)
    elif chosen == DOOR2:
        print("You live!")
        score = score +1 
        print(score)
sys.exit()