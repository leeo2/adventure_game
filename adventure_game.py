# Adventure Game
# Creators: Elizabeth Fuller, Olivia Lee
# Date Started: 10/30/19

import random
forest_monsters = ["werewolf", "goblin", "monster", "Moster", "Creepything"]  # 3 placeholder monsters, change these
swamp_monsters = ["slime", "kappa", "giant frog", "man-eating snake", "monster"]
mansion_monsters = ["ghost"]
forest_traps = ["pit fall", "hanging net", "snare", "snake pit", "gentrap"]

# monster win :
# 2 pt - fight
#  1pt - flee + reason
#  traps success
# 2 - wit
# 1 - strength

def die_roll_boss():
    # roll one 20 sided die, for boss fights
    die = random.randint(1, 20)
    return die


def die_roll_fight():
    # 6 sided die for player to roll during fights
    die = random.randint(1, 6)
    return die


def chance_roll():
    # either dice roll, or random int for chance of trap, monster, or free path.
    chance = random.randint(1, 10)
    return chance


def monster_select(list):
    # to select monster for regular fights. will have to send wanted list. forest, swamp, or mansion
    monster_number = random.randint(0, 4)
    x = 0
    while x < monster_number:
        x = x + 1
        for monster in list:
            creature = monster
    win = monster_encounter(creature) # win goes back to the path so it can continue or end the game
    return win


def monster_encounter(creature):
    # monster is picked. options for player
    print(f"A {creature} appears!")
    print("What do you do:\nFight [1]\nFlee [2]\nPanic [3]")
    choice = input("> ")
    choice = choice.strip()
    # player picked fight. go to fight function
    if choice == '1':
        win = monster_fight(creature)
    # player choose flee
    elif choice == '2':
# 50\50 1pt success, 0 pt + lose fail
        print("choose flee")
    # player picked panic automatic loss
    elif choice == '3':
        print('choose panic')
        win = 0
    # secret reason with option. 50\50 chance
    else:
        print(f"You decide to try and reason with the {creature}.")
        reason_chance = random.randint(0,1)
        if reason_chance == 0:
            print(f"You successfully reasoned with the {creature}.")

            win = 1
        else:
            print("failed to reason")
            win = 0
    # win goes back to previous function, see comment on monster_select to follow path of win
    return win


def monster_fight(creature):
    """ monster health, player health resets every fight
    player 'rolls' to determine damage dealt.
    monster attacks, player rolls to dodge. monster attack strength by random int
    loops till player or monster is dead"""
    monster_health = 125
    health = 100
    roll1 = die_roll_fight()
    print(f"You choose to stand your ground and fight.")
    print(f"Player health: {health}\n{creature.title()} health: {monster_health}")
    while monster_health != 0 or health != 0:

        print(f"\nYour move:\nYou roll the dice""")
        input(">")
        print(roll1)
        # damage calculations and inform player of what the damage is
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
        if monster_health < 0:
            monster_health = 0
        print(f"\nPlayer health: {health}\n{creature.title()} health: {monster_health}")
        # print health statuses. check to see if monster is dead. if yes stop loop
        if monster_health <= 0:
            print(f"You win!\nYou beat the {creature}! ")

            return 1
        # monster attack. player rolls to dodge. attack picked by random int
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
        if health < 0:
            health = 0
        # print health update. check to see if player is alive, no? - stop loop
        print(f"Player health: {health}\n{creature.title()} health: {monster_health}")
        if health < 0:
            print("You lose")
            return 0
    # loop till one is dead


def traps(traps):
    # to choose which trap from trap lists
    trap_number = random.randint(0, 4)
    x = 0
    while x < trap_number:
        x = x + 1
        for trap in traps:
            sprung_trap = trap
    escape = trap_escape(sprung_trap)
    return escape


def trap_escape(sprung_trap):
    # trap has been picked. how does play deal with it
    escape = 0
    print(f"You sprung a {sprung_trap}!")
    print("What do you do?")
    print("Use wits to escape [1]\nBlunt force your way out [2]\nPanic [3]")
    choice = input("> ")
    # think way out of the trap. 2\3 chance of success in escaping the trap
    if choice == '1':
        effect_wit = die_roll_fight()
        print(f"You decide to try and think your way out of the {sprung_trap}.")
        print("You roll the die...")
        input("> ")
        print(effect_wit)
        if effect_wit <= 4:
            print("success")
            escape = 1
        else:
            print("fail")
    # try to use strength to escape. 1\3 chance success
    elif choice == '2':
        effect_strength = die_roll_fight()
        print(f"You decide to use your raw strength to escape from the {sprung_trap}.")
        print("You roll the die...")
        input("> ")
        print(effect_strength)
        if effect_strength <= 2:
            print("success")
            escape = 1
        else:
            print("fail")
    # panic = automatic loss
    else:
        print("You lose your mind and fail to escape the trap. RIP")
    return escape


def welcome():
    print("""Welcome to out Adventure Game! You will be given a series of choices which 
    will ultimately all contribute to your fate. To begin, please enter your name: """)
    name = input()
    print(f"Welcome {name}!")

    print("The game will now begin.")



def swamp_path(score, name):
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
            print("As you were preoccupied by a particularly tricky bit of folliage...")
            print("You get caught by a trap!")
            success = traps(forest_traps)
            if success == 0:
                print("end game")
        else:
            # monster, add monster(list)
            # receives feedback on player winning or losing
            # if win continue down path if loss end game
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
        if spawn_left1 <= 3:
            # free
            print()
            print("""*interesting thing* 
Nothing else of note happens as you travel down the path. 
Eventually you come across a clearing.""")
        elif spawn_left1 <= 7:
            # trap
            # receives feedback on player winning or losing
            # if win continue down path if loss end game
            print("Trap activates")
            success = traps(forest_traps)
            if success == 0:
                print("end game")
        else:
            # monster, add monster(list)
            # receives feedback on player winning or losing
            # if win continue down path if loss end game
            print("While you were walking you hear the bushes rustle.")
            win = monster_select(forest_monsters)
            if win == 1:
                print("W")
            else:
                print("L")
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
    # right path swampy higher monster chance
    if swamp_choice2 == "1":
        spawn_right2 = chance_roll()
        if spawn_right2 <= 3:
            # free
            print()
            print("""things""")
        elif spawn_right2 <= 6:
            # trap
            # receives feedback on player winning or losing
            # if win continue down path if loss end game
            print("Trap activates")
            success = traps(forest_traps)
            if success == 0:
                print("end game")
        else:
            # monster, add monster(list)
            print("what happens before monster.")
            win = monster_select(swamp_monsters)
            # recieves feedbacl on player winning or losing
            # if win continue down path if loss end game
            if win == 1:
                print("W")
            else:
                print("L")
    # stable but higher traps
    elif swamp_choice2 == "2":
        spawn_left2 = chance_roll()
        if spawn_left2 <= 3:
            # free
            print()
            print("""things show up? 
Nothing else of note happens as you travel down the path. 
Eventually you come across a clearing.""")
        elif spawn_left1 <= 7:
            # trap
            print("Trap activates")
            success = traps(forest_traps)
            if success == 0:
                print("end game")
        else:
            # monster, add monster(list)
            print("monster indicator noises")
            win = monster_select(swamp_monsters)
            if win == 1:
                print("W")
            else:
                print("L")
    else:
        print("""You decide that instead of taking either path to walk around the clearing.
As you are walking you find a hidden path. This one looks well made, and is brightly lit.
You decide to take this path over the other two.
""")
    print("At the end of the path you come across a veil of vines, pushing it a side reveals a stone structure.")
    print("It seems to be some kind of altar. Perhaps it was made so people could give offerings to some god.")
    print("You walk over to the altar and hear a rumbling noise.")
    print("The ground starts falling away to reveal a huge snake pit.")
    print("There is one strip of land, one path back the way you came.")
    print("You start carefully start making your way down the path.")
    print("Suddenly a bright light appears in your way."
          "\nThe light fades to reveal...")
    swamp_boss(score, name)


def swamp_boss(score, name):
    boss_health = 175
    health = 100
    print("A lamia blocking your only escape."
          "\nShe beckons you closer..."
          "\nWhat do you do?"
          "\nCharge in for the attack [1]"
          "\nBecome seduced by the lamia [2]"
          "\nTry to talk to her [3]")
    choice = input("> ")
    if choice == '1':
        print(f"Lamia Health: {boss_health}\nPlayer Health: {health}")
        while boss_health != 0 or health != 0:
            roll1 = die_roll_fight()
            print(f"\nYour move:\nYou roll the dice""")
            input(">")
            print(roll1)
            if roll1 <= 3:
                damage = round(roll1 / 2 * 10)
                crit = random.randint(0, 3)
                if crit == 1:
                    damage = damage + 10
                print(f"You did {damage} damage to the lamia.")
                boss_health = boss_health - damage
            elif roll1 <= 5:
                damage = round((roll1 / 2 + roll1) * 10)
                crit = random.randint(0, 2)
                if crit == 1:
                    damage = damage + 10
                print(f"You did {damage} damage to the lamia.")
                boss_health = boss_health - damage
            else:
                damage = roll1 * 10 + 10
                crit = random.randint(0, 1)
                if crit == 1:
                    damage = damage + 10
                print(f"You did {damage} damage to the lamia.")
                boss_health = boss_health - damage
            if boss_health < 0:
                boss_health = 0
            print(f"Lamia Health: {boss_health}\nPlayer Health: {health}")
            if boss_health <= 0:
                print(f"You win!\nYou beat the lamia! ")
                score = score + 3
                print(" + 3")
                return
            print(f"Lamia's turn")
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
            if health < 0:
                health = 0
            print(f"Lamia Health: {boss_health}\nPlayer Health: {health}")
            if health <= 0:
                print("You lose")
                return
    elif choice == '2':
        print("She succeed in seducing you."
              "\nShe wrapped you up in her tail and carried you to her lair."
              "\nIt is a nice looking lair for a snake woman."
              "\nIt may be a cave, but it's decorated nicely with the bones of her past prey.")
        print("You became dinner"
              "\n\nYou lose!")
        end()
    else:
        # become friends
        print(f'''You decide to try talking to the lamia.
She seems startled by this, confusion settles over her face.
“You are talking to me? No one talks to me!”
She then explains that everyone that she came across tried to kill her
So as a defensive action she decided to hypnotize them and toss them into the snake pit.
“Oh my! I haven\'t even introduced myself. I am Vasugi.”
\nYou introduce yourself
“I am {name}, nice to meet you Vasugi.” 

Vasugi offers to take you back to her den for the night.
As it was getting quite late you took her up on the offer.

Vasugi's den was very cozy and looked well maintained.
You spend the night in a soft pile of furs.

After a small breakfast and chat with Vasugi, she escorts you back to civilization. 
As you part ways you promise to come visit sometimes.
''')
        print("You be came friends with Vasugi the Lamia!")
        score = score + 4
        print(" + 4")
        end()


def end():
    print("The game is now over")
    print(f"Your score is {score}")


# these are for my use of testing my path function
score = 0
name = "name"
run = swamp_path(score, name) # function caller to test swamp path
