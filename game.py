import time
import subprocess
import shutil
from pathlib import Path

IMAGES_DIR = Path(__file__).resolve().parent / "images"

if shutil.which("chafa") is None:
    print("NOTE: 'chafa' is not installed. Images won't display.")
    print("Install: winget install hpjansson.Chafa  (Windows)")
    print("         brew install chafa              (macOS)")
    print("         sudo apt install chafa          (Linux)")
    print()

def show(image_name):
    path = IMAGES_DIR / image_name
    if not path.exists():
        print(f"[image missing: {image_name}]")
        return
    try:
        subprocess.run(["chafa", str(path)], check=False)
    except FileNotFoundError:
        pass


## INTRO
name = input("What is your name?: ")
print("Welcome", name)
time.sleep(1)
show("forest.webp")
print("You are hiking deep in the forest at night completely alone")
time.sleep(4)
show("cabin1.webp")
print("Suddenly you stumble upon a two story abandoned cabin")
time.sleep(4)
print("From this point forward the choices you make will determine your fate")
time.sleep(4)
print("Upon seeing the cabin what is your next choice?")
time.sleep(2)
print("**** ENTER THE NUMBER FOR THE CHOICE YOU WOULD LIKE TO CHOOSE! ****")

def part2():
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    show("LivingRoom.png")
    print("Upon entering you see what used to be a cozy living space, now everything is covered in dust")
    time.sleep(2)
    print("An old electric fireplace sits in the middle of the room surrounded by taxidermy animals")
    time.sleep(4)
    print("In here you find £100 and an old mug, you store these in your backpack")
    time.sleep(2)
    print("What is your next choice?")
    flag = True
    while flag:
        print("1. Explore")
        print("2. Leave")
        choice = input("Choice: ")
        if choice == "2":
            print("You leave the forest safely with your items")
            print("GAME OVER")
            flag=False
        elif choice == "1":
            print("You see a doorway leading to another room, you walk inside")
            flag=False
            part3()
        else:
            print("Please enter 1 or 2")

def part3():
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    show("Kitchen.jpg")
    print("You see bowls, cups and plates scattered on a table, it's an old kitchen")
    time.sleep(2)
    print("There's food and drinks inside the cabinets and fridge, however they are all expired")
    time.sleep(2)
    print("You find an unexpired tin of sardines and a deck of playing cards on the table")
    flag = True
    while flag:
        print("1. Explore ")
        print("2. Leave")
        choice = input("Choice: ")
        if choice == "2":
            print("You safely exit the cabin with all of your items")
            print("GAME OVER")
            flag=False
        elif choice == "1":
            print("You see another door infront of you and decide to see what's inside")
            flag=False
            part4()
        else:
            print("Please enter 1 or 2")

def part4():
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    show("Bathroom.jpg")
    print("Inside you discover a bathroom, it's cleaner than you imagined")
    time.sleep(3)
    print("in the cabinets ther's nothing but old cleaning and hygeine products, you don't see anything worth keeping")
    flag = True
    while flag:
        print("1. Explore")
        print("2. Leave")
        choice = input("Choice: ")
        if choice == "2":
            print("You leave the cabin with all of your valuables")
            print("GAME OVER")
            flag=False
        elif choice == "1":
            print("You head back into the living room and see a staircase leading upstairs")
            time.sleep(2)
            print("You begin making your way up the stairs")
            flag=False
            part5()
        else:
            print("Please enter 1 or 2")

def part5():
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    show("topofstairs.jpg")
    print("At the top you see a small space with a window and a bookshelf")
    time.sleep(2)
    print("Inside the bookshelf you find a tiny connect 4 board game and a key with the label 'SAFE' on it")
    flag = True
    while flag:
        print("1. Explore ")
        print("2. Leave")
        choice = input("Choice: ")
        if choice == "2":
            print("You decide to leave and exit with all of your items")
            print("GAME OVER")
            flag=False
        elif choice == "1":
            print("You see a dark doorway to your right, curious, you head inside")
            flag=False
            part6()
        else:
            print("Please enter 1 or 2")

def part6():
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    show("corridor.jpg")
    print("You enter a hallway, there are 2 doors on your left, 2 on your right and one at the end of the corridor")
    time.sleep(2)
    print("There is nothing interesting in the hallway itself")
    flag = True
    while flag:
        print("1. Explore ")
        print("2. Leave")
        choice = input("Choice: ")
        if choice == "2":
            print("You decide to leave and exit with all of your items")
            print("GAME OVER")
            flag=False
        elif choice == "1":
            print("You proceed through the door on your left")
            flag=False
            part7()
        else:
            print("Please enter 1 or 2")

def part7():
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    show("bedroom.jpg")
    print("You enter a small bedroom, a painting above the bed and random debris on the floor")
    time.sleep(2)
    print("There are also 2 bookshelves")
    time.sleep(2)
    print("Inside you find an old pocket knife, an old £5 note and a silver ring")
    flag = True
    while flag:
        print("1. Explore ")
        print("2. Leave")
        choice = input("Choice: ")
        if choice == "2":
            print("You safely exit with all of your items")
            print("GAME OVER")
            flag=False
        elif choice == "1":
            print("You go back into the hallway and proceed through the door on your right")
            flag=False
            part8()
        else:
            print("Please enter 1 or 2")

def part8():
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    show("bedroom2.jpg")
    print("You enter the master bedroom, there is a large cabinet and dresser")
    time.sleep(2)
    print("Inside the cabinet you find a crossbow with no arrows, a pair of camoflague gloves and camoflague jacket")
    time.sleep(2)
    print("Inside the dresser you find an old expensive watch and a photo of a man holding a bear he has hunted")
    time.sleep(2)
    print("You also see a small safe sitting on the ground and unlock it with the key you found earlier")
    time.sleep(3)
    print("Inside you find £2000!")
    flag = True
    while flag:
        print("1. Explore ")
        print("2. Leave")
        choice = input("Choice: ")
        if choice == "2":
            print("You begin making your way out of the cabin")
            time.sleep(1)
            print("You realise you can't leave because the bear is standing in your way")
            time.sleep(1)
            show("bear.jpg")
            print("The bear is standing in your way")
            time.sleep(1)
            show("bear.jpg")
            print("The bear is standing in your way")
            time.sleep(1)
            show("bear.jpg")
            print("The bear is standing in your way")
            time.sleep(1)
            show("bear.jpg")
            print("The bear is standing in your way")
            time.sleep(1)
            show("bear.jpg")
            print("The bear is standing in your way")
            time.sleep(1)
            print("GAME OVER")
            flag=False
        elif choice == "1":
            show("corridor.jpg")
            print("You go back into the hallway and proceed through the door at the back left")
            flag=False
            part9()
        else:
            print("Please enter 1 or 2")

def part9():
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    show("office.jpg")
    print("You enter an old office room with paper and books scattered on the desk")
    time.sleep(2)
    print("There are some Bibles, dictionairies, hunting magazines, cook books and even comics")
    time.sleep(2)
    print("You also find deer antlers, a fire starter and a decent flashlight but no batteries")
    time.sleep(2)
    flag = True
    while flag:
        print("1. Explore ")
        print("2. Leave")
        choice = input("Choice: ")
        if choice == "2":
            print("You leave the cabin safely with your items")
            print("GAME OVER")
            flag=False
        elif choice == "1":
            show("corridor.jpg")
            print("You go back into the hallway")
            flag=False
            part10()
        else:
            print("Please enter 1 or 2")

def part10():
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    show("corridor.jpg")
    print("Choose which door")
    flag = True
    while flag:
        print("1. Back Right ")
        print("2. End of corridor")
        choice = input("Choice: ")
        if choice == "2":
            print("You enter the door at the end of the corridor")
            flag=False
            endofcor()
        elif choice == "1":
            show("corridor.jpg")
            print("You Enter the last door on the right")
            flag=False
            backright()
        else:
            print("Please enter 1 or 2")

def backright():
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    show("backriht.jpg")
    print("You enter a small bedroom with a bookshelf above the bed and old clothes on the walls")
    time.sleep(2)
    print("There is also a dusty dresser with a vase of ashes on top, there is nothing in the dresser")
    time.sleep(2)
    print("However in the drawer beside the bed, you find a necklace, earrings and a pen")
    time.sleep(2)
    print("You then take your items and leave the cabin safely")
    print(" ***** VICTORY *****")

def endofcor():
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(3)
    show("bear2.jpg")
    time.sleep(3)
    show("bear3.jpg")
    time.sleep(3)
    show("bear4.jpg")
    time.sleep(3)
    print("you should have left.....")


flag = True
while flag:
    print("1. Explore (Recommended)")
    print("2. Leave")
    choice = input("Choice: ")
    if choice == "2":
        print("You decided not to go in, you begin making your way out of the forest")
        print("GAME OVER")
        flag=False
    elif choice == "1":
        print("Curiosity got the better of you, you begin making your way into the cabin")
        flag=False
        part2()
    else:
        print("Please enter 1 or 2")