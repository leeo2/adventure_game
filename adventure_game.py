# Adventure Game
# Creators: Elizabeth Fuller, Olivia Lee
# Date Started: 10/30/19

import random


def die_roll():
    # roll one 20 sided die, for boss fights
    die = random.randint(1, 20)
    return die


def chance_roll():
    # either dice roll, or random int for chance of trap, monster, or free path. change if statements if values change
    chance = random.randint(1, 10) # what range do we want to use? if dice 2-12? if not is 1-10 fine?
    return chance


def welcome():
    print("""Welcome to out Adventure Game! You will be given a series of choices which 
    will ultimatly all contribute to your fate. To begin, Please enter your name: """)
    name = input()


def swamp_path():
    # Path to go to the swamp. walking down chosen path, first swamp path fork dialog
    print("You walk down the path taking in the scenery.\nYou come across another fork in the road.")
    print("The path splits left and right.\nThe right path is overgrown and looks very untrodden.")
    print("The left path is poorly lit from the tree canopy. Better light a torch!")
    print("Which way do you go:\nRight [1]\nLeft [2]")
    # ask for player choice 3 options, right, left, and get lost by leaving the path
    #
    swamp_choice1 = input("> ")
    swamp_choice1 = swamp_choice1.strip()

    if swamp_choice1 == "1":
        # higher monster chance
        print("\nYou took the path on the right.\nYou carefully watch your step as to not get tangled in the undergrowth.")
        # determine if monster appears, trap activates, or if player misses any impeding obstacles
        spawn_right1 = chance_roll()
        print(spawn_right1) # statement to check random int
        if spawn_right1 <= 3:
            # free
            print()
            print("""The undergrowth almost trips you up and you find a rare flower. 
Nothing else of note happens as you travel down the path. 
Eventually you come across a clearing.""")
        elif spawn_right1 <= 6:
            # trap
            print("Trap activates")
        else:
            # monster, add monster(list)
            print("While you were walking you hear the bushes rustle. Out jumps a {forest_monster}!")
            print("What do you do?\nFight [1]\nFlee for you life [2]\nPanic [3]")
            swamp_fight1 = input("> ")
            swamp_fight1 = swamp_fight1.strip()

    elif swamp_choice1 == "2":
        # higher trap chance
        print("Went Left")
        spawn_left1 = chance_roll()
        print(spawn_left1)
    else:
        # left the path and get lost. options from here- end game or possibly find next path split
        print("Um... this is not the path... turn back... great now your lost")
    # paths converge and then there is another fork with 2 paths
    print("You decide to take a quick break and look around the clearing.")
    print("""As you do you realize the other path probably ends here as well. 
You could have taken either and still gotten here!""")
    print("It looks like there is a swamp up ahead. Gross... mud and icky things everywhere.")
    print("One path goes of to the right and looks very marshy. It doesn't look very stable, watch your step!")
    print("The other veers off to the left. This one looks more stable and considerably drier.")
    print("Which path do you think you should take?\nRight [1]\nLeft [2]")
    swamp_choice2 = input("> ")
    swamp_choice2 = swamp_choice2.strip()
    if swamp_choice2 == "1":
        print("Right")
    elif swamp_choice2 == "2":
        print("Left")
    else:
        print("""You decide that instead of taking either path to walk around the clearing.
As you are walking you find a hidden path. This one looks well made, and is brightly lit.
You decide to take this path over the other two.
""")



run = swamp_path() # function caller to test swamp path
