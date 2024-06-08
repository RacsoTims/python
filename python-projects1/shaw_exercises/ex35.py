from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input("> ")
    if choice.isnumeric():
        how_much = int(choice)
    else:
        print("Man, learn to type a number.")
        gold_room()

    if how_much == 0:
        print("You leave with nothing. You are too modest!")
        exit(0)
    elif how_much < 50:
        print("Nice, you're not greedy, you win! You can relax and spend the gold however you see fit.")
        exit(0)
    else:
        dead("You greedy bastard! You were tracked down and killed by the self-described 'owner' of the gold.")


def bear_room():
    print("""There is a bear here.
The bear has a bunch of honey.
The fat bear is in front of another door.
How are you going to move the bear?""")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you, then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("""The bear has moved from the door.
You can go through it now.""")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your legs off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("""Here you see the great evil Cthulhu.
He, it, whatever stares at you and you go insane.
Do you flee for your life or eat your head?""")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good job.")
    exit(0)

def start():
    print("""You are in a dark room.
There is a door to your right and left.
Which one do you take?""")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    elif choice == "skip":
        gold_room()
    else:
        dead("You stumble around the room until you starve.")


start()
