#!/usr/bin/env python3

def enter_name_ready():
    print('*****\n*****\n*****\n*****\n\n\n\tWELCOME TO THE WEST TAGHKONIC DINER ADVENTURE GAME!!!\n\n\n*****\n*****\n*****\n*****\n')
    choice = input(f'Have you played this game before?\n 1: Yes \n 2: No\n')
    while choice not in ['1', '2']:
        choice = input(f'\nOOPS! You entered a wrong choice. Try again: \nHave you played this game before?\n 1: Yes \n 2: No\n')
    if choice == '2':
        read_rules = input(f'Would you like to hear the rules before we begin?\n 1: Yes \n 2: No\n')
        while read_rules not in ['1', '2']:
            read_rules = input(f'\nOOPS! You entered a wrong choice. Try again: \nWould you like to read the rules?\n 1: Yes \n 2: No\n')
        if read_rules == '1':
            read_the_rules()
    return get_user_name()


def read_the_rules():
    rules = """
        - Every customer who comes in is thirsty and hungry
        - Their thirst and hunger levels will be added to your stress levels
        - You can serve them whenever you like and give them a check whenever you like!
        - Giving them food makes you and them less stressed
        - Checking them out makes you and them less stressed AND if you served them, it gives you money!
        - THE TRICK IS THAT YOU DO NOT KNOW HOW HUNGRY OR THIRSTY THEY ARE!
        - OR how much money they are going to spend
        - The only way to figure these things out is to ask them
        - But once you ask, or serve them, or check them out, BE READY!
        - Another customer is already at the door.
        - If you get too stressed (MAX 50 STRESS) or the restruant gets too full, it's GAME OVER!
    """
    print(rules)


def get_user_name():
    print('\n**********\nTime to get the show on the road!\n**********\n')
    user_name = input('Please enter your name: ').title()
    print('\n\tNice to meet you, ' + user_name + '!!! \n\n')
    print('\tAlrighty...\n\n\tReady?\n\tSet?!\n\tHERE WE GO!!\n\n*****\n*****')
    return user_name
    

def choose_a_task():
    choice = input(f'What action would you like to take? Type your response:\n 1: Assess a customer\'s hunger and thirst \n 2: Take an order \n 3: Give someone the check\n')
    while choice not in ['1', '2', '3']:
        choice = input(f'\nOOPS! You entered a wrong choice. Try again:\n 1: Assess a customer\'s hunger and thirst \n 2: Take an order \n 3: Give someone the check\n')
    return int(choice)
    

def game_over(user_name, money, stress, seated_customers):
    if stress >= 50:
        print('\n\n**********OH NO!! Looks like you got a little too stressed from everything that is going on!!**********\n\n')
    elif len(seated_customers) == 5:
        print('\n\n**********OH NO!! Looks like all the tables are full! More customers are coming and there is no where for them to sit!!**********\n**********STRESS GOES THROUGH THE ROOF!**********\n\n')
    else:
        print('\n\n**********OH NO!! DOUBLE STRESS!! You are too stressed AND there is no place to sit the incoming customers!! NOO!!!!**********\n\n')
    print(f'\n\n\n\t********** GAME OVER!!!**********\n\n\nIt looks like you made a total of ${money}\n\nBetter luck next time, {user_name}!')
    with open('highscores.txt', mode='a', encoding='utf-8') as highscores:
        highscores.write(f'Name: {user_name}\nScore: {money}\n')