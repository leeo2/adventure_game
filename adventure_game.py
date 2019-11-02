# Adventure Game
# Creators: Elizabeth Fuller, Olivia Lee
# Date Started: 10/30/19

import random
forest_monsters = ["werewolf", "goblin", "monster", "Moster", "Creepything"]  # 3 placeholder monsters, change these
swamp_monsters = ["slime", "kappa", "monster", "monster", "monster"]
mansion_monsters = []
collected_items = []


def die_roll_boss():
    # roll one 20 sided die, for boss fights
    die = random.randint(1, 20)
    return die


def die_roll_fight():
    # 6 sided die for player to roll during fights
    die = random.randint(1, 6)
    return die


def chance_roll():
    # either dice roll, or random int for chance of trap, monster, or free path. change if statements if values change
    chance = random.randint(1, 10) # what range do we want to use? if dice 2-12? if not is 1-10 fine?
    return chance


def monster_select(list):
    # to select monster for regular fights. will have to send wanted list. forest, swamp, or mansion
    monster_number = random.randint(0, 4)
    x = 0
    while x < monster_number:
        x = x + 1
        for monster in list:
            creature = monster
    win = monster_encounter(creature)
    return win


def monster_encounter(creature):
    print(f"A {creature} appears!")
    print("What do you do:\nFight [1]\nFlee [2]\nPanic [3]")
    choice = input("> ")
    choice = choice.strip()
    if choice == '1':
        win = monster_fight(creature)

    elif choice == '2':
        print("choose flee")

    elif choice == '3':
        print('choose panic')
        win = 0
    else:
        print(f"You decide to try and reason with the {creature}.")
        reason_chance = random.randint(0,1)
        if reason_chance == 0:
            print(f"You successfully reasoned with the {creature}.")

            win = 1
        else:
            print("failed to reason")
            win = 0
    return win


def monster_fight(creature):
    monster_health = 150
    health = 100
    roll1 = die_roll_fight()
    print(f"You choose to stand your ground and fight.")
    print(f"Player health: {health}\n{creature.title()} health: {monster_health}")
    while monster_health != 0 or health != 0:

        print(f"\nYour move:\nYou roll the dice""")
        input(">")
        print(roll1)
        if roll1 <= 3:
            damage = round(roll1 / 2 * 10)
            print(f"You did {damage} damage to the {creature}.")
            monster_health = monster_health - damage
        elif roll1 <= 5:
            damage = round((roll1 / 2 + roll1) * 10)
            print(f"You did {damage} damage to the {creature}.")
            monster_health = monster_health - damage
        else:
            damage = roll1 * 10 + 10
            print(f"You did {damage} damage to the {creature}.")
            monster_health = monster_health - damage

        print(f"\nPlayer health: {health}\n{creature.title()} health: {monster_health}")
        if monster_health == 0:
            print(f"You win!\nYou beat the {creature}! ")

            return 1
        print(f"{creature.title()}'s turn")
        attack1 = chance_roll()
        dodge = die_roll_fight()
        input("You roll for a chance to dodge\n>")
        print(dodge)
        if dodge <= 3:
            print("dodges")
        elif attack1 == 1:
            health = health - 10
            print("attack of 10")
        elif attack1 <= 3:
            print("attack of 20")
            health = health - 20
        elif attack1 <= 6:
            print("attack of 30")
            health = health - 30
        elif attack1 <= 9:
            print("attack of 40")
            health = health - 40
        else:
            print("attack of 50")
            health = health - 50
        print(f"Player health: {health}\n{creature.title()} health: {monster_health}")
        if health == 0:
            print("You lose")
            return 0





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
            print("While you were walking you hear the bushes rustle.")
            win = monster_select(forest_monsters)
            if win == 1:
                print("W")
            else:
                print("L")




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
