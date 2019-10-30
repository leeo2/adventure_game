# Adventure Game
# Creators: Elizabeth Fuller,
# Date Started: 10/30/19

# My email is leeo@hartwick.edu
import random


def die_roll():
    # roll one 20 sided die, for boss fights
    die = random.randint(1, 20)
    return die


def chance_roll():
    # either dice roll, or random int for chance of trap, monster, or free path
    chance = random.randint(1, 10) # what range do we want to use? if dice 2-12? if not is 1-10 fine?
    return chance


def swamp_path():
    print("You walk down the path taking in the scenery.\nYou come across another fork in the road.")
    print("The path splits left and right.\nThe right path is overgrown and looks very untrodden.")
    print("The left path is poorly lit from the tree canopy. Better light a torch! ")
    print("Which way do you go:\nRight [1]\nLeft [2]")
    swamp_choice1 = input("> ")
    swamp_choice1 = swamp_choice1.strip()
    swamp_choice1 = input(swamp_choice1)
    if swamp_choice1 == 1:
        print("Went right")  # place holder text
    elif swamp_choice1 == 2:
        print("Went Left")
    else:
        print("Um... this is not the path... turn back... great now your lost")

    print("One path goes of to the right and looks very marshy. It doesn't look very stable, watch your step!")
    print("The other veers off to the left. This one looks more stable and considerably drier.")


swamp_path() # function caller to test swamp path
