#Random library
import random
# Helper function
def name_to_number(name):
    if name=='rock':
        return 0
    elif name=='spock':
        return 1
    elif name=='paper':
        return 2
    elif name=='lizard':
        return 3
    elif name=='scissors':
        return 4
# Another helper function
def number_to_name(number):
    if number==0:
        return 'rock'
    elif number==1:
        return 'spock'
    elif number==2:
        return 'paper'
    elif number==3:
        return 'lizard'
    elif number==4:
        return 'scissors'
# Game function
def rpsls(choice):
    print("\n\nYou choose: %s" %player_choice)
    player_number=name_to_number(choice)
    comp_number=random.randrange(1,4)
    comp_choice=number_to_name(comp_number)
    print("Computer chooses: %s" % comp_choice)
    res=player_number-comp_number
    if res !=0:
        if res<0 and res>=-2:
            print ('You Lose!')
        else:
            print('You win!')
    else:
        print("Oops! It's a Tie.")

#A list of valid choices
choices=['rock','paper','scissors','lizard','spock']

#user input prompt
player_choice = input('Enter your choice: ')
if player_choice in choices:
    rpsls(player_choice)
else:
    print('First, you should know the rules.')
