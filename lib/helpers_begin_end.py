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
        GENERAL
        *******
        Make sure your stress level stays below 50 AND that the restaurant has enough tables available!!

        
        HOW TO PLAY
        *******
        - First : You must seat a customer
        To seat a customer, simply pick an available table by entering the number. Then press enter
        You will then be notified how stressful this customer is!

        - Second: Make a choice!
        You can either assess a customer's needs, take their order (drink or meal), or give them a receipt.
        Couple things to note here:
            - Assessing a customer's needs is the only way to see what is stressing them (thirst or hunger)
            - You can take their order WITHOUT assessing their needs
            - When you check them out, you can reduce their stress from your stress.

        - Third: Repeat!!
        Watch out! Another customer is likely on their way! And the cycle starts again...

        
        HOW TO SCORE POINTS:
        *******
        Every drink or meal you serve a customer has an assigned value.
        When you check out the customer, you will earn that money (ONLY IF YOU SERVED THEM SAID ITEM!)
        Assessing a customer's needs is the only way to see the value of their orders ahead of time


        BEST OF LUCK!!!
    """
    print(rules)


def get_user_name():
    print('\n**********\nTime to get the show on the road!\n**********\n')
    user_name = input('Please enter your name: ').title()
    print('\n\tNice to meet you, ' + user_name + '!!! \n\n')
    print('\tAlrighty...\n\n\tReady?\n\tSet?!\n\tHERE WE GO!!\n\n*****\n*****')
    return user_name
    

def choose_a_task():
    choice = input(f'What action would you like to take? Type your response:\n 1: Assess a customer\'s hunger and thirst \n 2: Take an order \n 3: Give someone the check\n 4: GIVE UP!')
    while choice not in ['1', '2', '3', '4']:
        choice = input(f'\nOOPS! You entered a wrong choice. Try again:\n 1: Assess a customer\'s hunger and thirst \n 2: Take an order \n 3: Give someone the check\n 4: GIVE UP!')
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
        highscores.write(f'\nName: {user_name}\nScore: {money}\n')