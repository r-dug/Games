from sys import exit

def gold_room(chances):
    chances = chances
    print("""

    WOWZA! This room is filled with gold bars. how many do you take?

    """)

    while chances >= 0:
        choice = input("> ")

        if "0" in choice or "1" in choice:
            how_much = int(choice)
        elif "love" in choice:
            print("You're so lovely. you win!")
            exit(0)
        else:
            print("Man... learn how to respond reasonably. \nI'm taking a chance for your insolence!\nChances: ", chances)
            chances -= 1

        if how_much < 50:
            print(f"Nice, you're not that greedy. You win, with {how_much} gold bars!")
            exit(0)
        else:
            print("You greasy little fuck! Don't take so much gold!\nChances:", chances)
            chances -= 1
    dead("You were a stupid, greedy little cunt muffin, so you died.")

def bear_room(chances):
    chances = chances
    print(f"""

There is a bear in here...
The bear has some honey and
Is sitting in front of another door...
How will you move this bear??

""")
    bear_moved = False
    while True and chances >= 0 and chances >= 0:
        print(f"chances: {chances}")
        choice = input("Make your move\n> ").lower()
        hostile_words = ["take", "fight", "attack"]

        if hostile_words[0] in choice or hostile_words[1] in choice or hostile_words[2] in choice:
            chances -= 1
            for value in hostile_words:
                choice = choice.replace(value, '')
            print("the bear politely asks you to try again.")
        elif "love" in choice and not bear_moved:
            print("the bear has moved \ngo on through, ok?")
            bear_moved = True
        elif "love" in choice and bear_moved:
            chances -= 1
            print("The bear gets annoyed and eats you whole!")
            start(chances)
        elif "ok" in choice and bear_moved:
            gold_room(chances)
        else:
            print("The bear is unmoved...")
            chances -= 1
    dead("You died triying to move a friendly bear...\nThe bear ate you, bear hater!")
def cthulhu_room(chances):
    chances = chances
    print("""

Here you see the great and evil Cthulhu!
It stares at you and you go insane...
Do you flee or stay
""")

    while chances >= 1:
        print(f"chances: {chances}")
        choice = input("> ").lower()
        if "flee" in choice:
            print("One cannot flee from the mighty Cthulhu")
            chances -= 1
        elif "stay" in choice:
            print("Well that was tasty... Cthulhu made you eat your own soul, then leave.")
            start(chances)
        elif "kill" or "fight" in choice:
            print("You've defeated Cthulhu...\n")
            bear_room(chances)
        else:
            print("Cthulhu the mighty has taken a chance from you, puny mortal.")
            chances -= 1
    dead("you died in the Cthulhu Dungeon!")

def dead(why):
    print(why, "greaaaat...")
    exit(0)

def start(difficulty):
    chances = difficulty
    print("""
You have found yourself in a dark room...
There is a door to your right and one to your left too...
Inscribed on the floor is a riddle:

    Choose poorly and perish
    The honey ain't sweet as love untold
    With Cthulhu, dance or die
    Choose wisely and maybe win gold

""")

    while chances >= 0:
        print(f"You have {chances} chances, human.\nWhat will you do?")
        choice = input("> ").lower()
        if "left" in choice:
            bear_room(chances)
        elif "right" in choice:
            cthulhu_room(chances)
        elif "love" in choice:
            gold_room(chances)
        else:
            chances -= 1
            print("you stumble around the room until you starve and lose a life!")
    dead("You LOSE!")
def difficulty_select():
    validInt = False

    while not validInt:
        difficulty = input("how many chances between 3 and 6 would you like to get through this game?")
        if difficulty.isdigit():
            validInt = True
            difficulty = int(difficulty)
            start (difficulty)
        else:
            print("Not a number. Try again!\n")

    while difficulty > 6 or difficulty < 3:
        print("A number between 3 and 6. Try again!\n")
        validInt = False

        while not validInt:
            difficulty = input("how many chances between 3 and 6 would you like to get through this game?")
            if difficulty.isdigit():
                validInt = True
                difficulty = int(difficulty)
                start(difficulty)
            else:
                print("Not a number. Try again!\n")
difficulty_select()
