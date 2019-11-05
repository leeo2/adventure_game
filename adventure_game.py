# Adventure Game
# Creators: Elizabeth Fuller, Olivia Lee
# Date Started: 10/30/19


#if score doesn't work just trash it and make it so not dying means you win.
import random
forest_monsters = ["werewolf", "goblin", "ogre", "black phoenix", "creepything"]  # 3 placeholder monsters, change these
swamp_monsters = ["slime", "kappa", "giant frog", "man-eating snake", "swarm of locus"]
mansion_monsters = ["ghost", "zombie", "mummy", "spider nest", "snake"]
mansion_traps = ["trap door", "trap", "hanging net", "Another trap", "pit of snakes"]
forest_traps = ["pit fall", "hanging net", "snare", "snake pit", "quicksand"]
score = 0

# monster win :
# 2 pt - fight
#  1pt - flee + reason
#  traps success
# 2 - wit
# 1 - strength


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
    print(f"You choose to stand your ground and fight.")
    print(f"Player health: {health}\n{creature.title()} health: {monster_health}")
    while monster_health != 0 or health != 0:
        roll1 = die_roll_fight()
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
            print("You managed to dodge the incoming attack.")
        elif attack1 == 1:
            health = health - 10
            print(f"{creature} attacks you and deals 10 damage.")
        elif attack1 <= 3:
            print(f"{creature} attacks you and deals 20 damage.")
            health = health - 20
        elif attack1 <= 6:
            print(f"{creature} attacks you and deals 30 damage.")
            health = health - 30
        elif attack1 <= 9:
            print(f"{creature} attacks you and deals 40 damage.")
            health = health - 40
        else:
            print(f"{creature} attacks you and deals 50 damage.")
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
            print(f"You successfully escaped the {sprung_trap}!")
            escape = 1
        else:
            print(f"You failed to escape the {sprung_trap}.")
    # try to use strength to escape. 1\3 chance success
    elif choice == '2':
        effect_strength = die_roll_fight()
        print(f"You decide to use your raw strength to escape from the {sprung_trap}.")
        print("You roll the die...")
        input("> ")
        print(effect_strength)
        if effect_strength <= 2:
            print(f"You successfully escaped the {sprung_trap}!")
            escape = 1
        else:
            print(f"You failed to escape the {sprung_trap}.")
    # panic = automatic loss
    else:
        print("You lose your mind and fail to escape the trap. RIP")
        end()
    return escape


def welcome():
    print("""Welcome to out Adventure Game! You will be given a series of choices which 
will ultimately all contribute to your fate. To begin, please enter your name: """)
    name = input("> ")
    print(f"Welcome {name}!")

    print("The game will now begin.")
    print("From where you begin, you need to choose if you would like to take the path on the right [1] or left [2]")
    choice = int(input("> "))
    if choice == 1:
        swamp_path(score, name)
    elif choice ==2:
        mansion_path(name, score)
    else:
        print("Invalid choice. I will now send you on the path to the right.")


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

        if spawn_right1 <= 3:
            # free
            print()
            print("""The undergrowth almost trips you up and you find a rare flower. 
Nothing else of note happens as you travel down the path. 
Eventually you come across a clearing.""")
        elif spawn_right1 <= 6:
            # trap
            print("As you were preoccupied by a particularly tricky bit of foliage...")
            print("You get caught by a trap!")
            success = traps(forest_traps)
            if success == 0:
                end(score)
            else:
                print("You continue down the path and find a clearing.")
        else:
            # monster, add monster(list)
            # receives feedback on player winning or losing
            # if win continue down path if loss end game
            print("While you were walking you hear the bushes rustle.")
            win = monster_select(forest_monsters)
            if win == 1:
                print("After beating the creature you continue down the path.")
                print("The path starts clearing and ends in a great clearing.")
            else:
                end(score)

    elif swamp_choice1 == "2":
        # higher trap chance
        print("Went Left")
        spawn_left1 = chance_roll()

        if spawn_left1 <= 3:
            # free
            print()
            print("""You get scared when you see something out the corner of your eye... it was a shadow!
You are now embarrassed that you goth scared by a shadow.
Nothing else of note happens as you travel down the path. 
Eventually you come across a clearing.""")
        elif spawn_left1 <= 7:
            # trap
            # receives feedback on player winning or losing
            # if win continue down path if loss end game
            print("You got tripped by something in the dark")
            print("There is a grinding noise...")
            success = traps(forest_traps)
            if success == 0:
                end(score)
            else:
                print("You continue down the path while looking out for more traps.")
                print("No more traps activate and the path lightens as it comes upon a clearing.")
        else:
            # monster, add monster(list)
            # receives feedback on player winning or losing
            # if win continue down path if loss end game
            print("While you were walking a shadow jumps you!")
            win = monster_select(forest_monsters)
            if win == 1:
                print("You continue cautiously down the path until you reach a clearing.")
            else:
                end(score)
    else:
        # left the path and get lost. options from here- end game or possibly find next path split
        print("Um... this is not the path... turn back... great now your lost")
        end()
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
            print("""You head down the path and try to be careful not wanting to step in any sink holes.
Yuck! One miss step is all it takes to get mud in your shoe.
After trying to get rid of most of the mud, 
you suck it up though and keep going.""")
        elif spawn_right2 <= 6:
            # trap
            # receives feedback on player winning or losing
            # if win continue down path if loss end game
            print("With all of the wet and mushy ground you fail to spot a tripwire.")
            success = traps(forest_traps)
            if success == 0:
                end(score)
            else:
                print("Keeping a closer eye out you make your way to the dryer ground at the end of the path.")

        else:
            # monster, add monster(list)
            print("Keeee! A blur crosses your vision.")
            win = monster_select(swamp_monsters)
            # recieves feedbacl on player winning or losing
            # if win continue down path if loss end game
            if win == 1:
                print("Keeping an eye out for anymore swamp monster you continue onward.")
            else:
                end(score)
    # stable but higher traps
    elif swamp_choice2 == "2":
        spawn_left2 = chance_roll()
        if spawn_left2 <= 3:
            # free
            print()
            print("""As you thought this path was stable you don't watch very carefully.
You get tripped up on a tree root.""")
        elif spawn_left1 <= 7:
            # trap
            print("""As you thought this path was stable you don't watch very carefully.
And as such you don't notice the pressure plate.""")
            success = traps(forest_traps)
            if success == 0:
                print("end game")
            else:
                print("With much more care you keep walking down the path.")
        else:
            # monster, add monster(list)
            print("The water beside the path begins to bubble and erupts in a great splash.")
            win = monster_select(swamp_monsters)
            if win == 1:
                print("You shakily continue down the path.")
            else:
                end(score)
    else:
        print("""You decide that instead of taking either path you walk around the clearing.
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
                print("You manage to dodge the incoming attack.")
            elif attack1 == 1:
                health = health - 10
                print("The lamia attacks you and deals 10 damage.")
            elif attack1 <= 3:
                print("The lamia attacks you and deals 20 damage.")
                health = health - 20
            elif attack1 <= 6:
                print("The lamia attacks you and deals 30 damage.")
                health = health - 30
            elif attack1 <= 9:
                print("The lamia attacks you and deals 40 damage.")
                health = health - 40
            else:
                print("The lamia attacks you and deals 50 damage.")
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


def mansion_path(name, score):
    print("You are heading towards a clearing in the middle of the forest")
    print("What's that? Is that a mansion?")
    print("You need to choose. \nWould you like to enter the mansion? [1] \n Or would you like to walk around the mansion? [2]")
    mansion_choice1 = int(input(">"))
    if mansion_choice1 == 1:
        print("You chose to enter the mansion")
        print("You creep up the rickety porch steps")
        print("You gingerly knock on the door, the door creaks open from the force of your knock.")
        monster1 = chance_roll()

        if monster1 <= 3:
            print("There is nothing on the other side of the door. You enter to explore.")
        elif monster1 <= 6:
            success = traps(mansion_traps)
            if success == 0:
                end(score)
        else:
            print("You continue even further into the house.")
    elif mansion_choice1 == 2:
        monster2 = chance_roll()
        if monster2 <= 3:
            print("You see a shadow and wonder what it is...")
            print("Phew, It's just a brooms shadow")
        elif monster2 <= 7:
            print("What was that?")
            success = traps(mansion_traps)
            if success == 0:
                end(score)
            else:
                print("You continue down the hallway while looking out for more traps.")
        else:
            print("While you were walking a shadow jumps you!")
            win = monster_select(mansion_monsters)
            if win == 1:
                print("You continue deeper into the house...")
            else:
                end(score)
    else:
        print("I don't think that was an option...")
        print("You need to choose. \nWould you like to enter the mansion? [1] \n Or would you like to walk around the mansion? [2]")
        mansion_choice1 = int(input(">"))

        if mansion_choice1 == 1:
            print("You chose to enter the mansion")
            print("You creep up the rickety porch steps")
            print("You gingerly knock on the door, the door creaks open from the force of your knock.")
            monster1 = chance_roll()

            if monster1 <= 3:
                print("There is nothing on the other side of the door. You enter to explore.")
            elif monster1 <= 6:
                success = traps(mansion_traps)
                if success == 0:
                    end(score)
            else:
                print("You continue even further into the house.")
        elif mansion_choice1 == 2:
            monster2 = chance_roll()
            if monster2 <= 3:
                print("You see a shadow and wonder what it is...")
                print("Phew, It's just a brooms shadow")
            elif monster2 <= 7:
                print("What was that?")
                success = traps(mansion_traps)
                if success == 0:
                    end(score)
                else:
                    print("You continue down the hallway while looking out for more traps.")
            else:
                print("While you were walking a shadow jumps you!")
                win = monster_select(mansion_monsters)
                if win == 1:
                    print("You continue deeper into the house...")
                else:
                    end(score)
    print("Would you like to turn right [1] or left [2]")
    mansion_choice2 = int(input("> "))
    if mansion_choice2 == 1:
        monster3 = chance_roll()
        if monster3 <= 3:
            print("The hallway is empty, you are in the clear.")
        elif monster3 <= 6:
            success = traps(mansion_traps)
            if success == 0:
                end(score)
        else:
            print("You continue even further into the house.")
    elif mansion_choice2 == 2:
        monster4 = chance_roll()
        if monster4 <= 3:
            print("You see a shadow and wonder what it is...")
            print("Phew, It's just a shadow")
        elif monster4 <= 7:
            print("What was that?")
            success = traps(mansion_traps)
            if success == 0:
                end(score)
            else:
                print("You continue down the hallway while looking out for more traps.")
        else:
            print("While you were walking a shadow jumps you!")
            win = monster_select(mansion_monsters)
            if win == 1:
                print("You continue deeper into the house...")
            else:
                end(score)
    else:
        print("Wrong choice, this will lead to your demise.")
        end(score)
    mansion_boss()


def mansion_boss(score, name):
    boss_health = 175
    health = 100
    print("""Oh no! There is a huge monster ahead? What do you want to do?
        \nCharge in for the attack [1]"
        \nBecome seduced by the monster [2]"
        \nTry to talk to it [3]""")
    choice = input("> ")
    if choice == '1':
        print(f"Monster Health: {boss_health}\nPlayer Health: {health}")
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
                print(f"You did {damage} damage to the monster.")
                boss_health = boss_health - damage
            elif roll1 <= 5:
                damage = round((roll1 / 2 + roll1) * 10)
                crit = random.randint(0, 2)
                if crit == 1:
                    damage = damage + 10
                print(f"You did {damage} damage to the monster.")
                boss_health = boss_health - damage
            else:
                damage = roll1 * 10 + 10
                crit = random.randint(0, 1)
                if crit == 1:
                    damage = damage + 10
                print(f"You did {damage} damage to the monster.")
                boss_health = boss_health - damage
            if boss_health < 0:
                boss_health = 0
            print(f"Monster Health: {boss_health}\nPlayer Health: {health}")
            if boss_health <= 0:
                print(f"You win!\nYou beat the Monster! ")
                score = score + 3
                print(" + 3")
                return
            print(f"Monster's turn")
            attack1 = chance_roll()
            dodge = die_roll_fight()
            input("You roll for a chance to dodge\n>")
            print(dodge)
            if dodge <= 3:
                print("You manage to dodge the incoming attack.")
            elif attack1 == 1:
                health = health - 10
                print("The monster attacks you and deals 10 damage.")
            elif attack1 <= 3:
                print("The monster attacks you and deals 20 damage.")
                health = health - 20
            elif attack1 <= 6:
                print("The monster attacks you and deals 30 damage.")
                health = health - 30
            elif attack1 <= 9:
                print("The monster attacks you and deals 40 damage.")
                health = health - 40
            else:
                print("The monster attacks you and deals 50 damage.")
                health = health - 50
            if health < 0:
                health = 0
            print(f"Monster Health: {boss_health}\nPlayer Health: {health}")
            if health <= 0:
                print("You lose")
                return
    elif choice == '2':
        print("Oh no, she looks pretty hungry... She has decided to eat you for her next meal"
              "\n\nYou lose!")
        end()
    else:
        print("You become friends!")
        score = score + 4
        print(" + 4")
        end()



def end():
    print("The game is now over")
    print(f"Your score is {score}")

welcome()
# these are for my use of testing my path function
score = 0
win = 0
name = "name"
run = swamp_path(score, name) # function caller to test swamp path
