#!/usr/bin/env python3

def enter_name_ready():
    print('*****\n*****\n*****\n*****\n\n\n\tWELCOME TO THE WEST TAGHKONCI DINER ADVENTURE GAME!!!\n\n\n*****\n*****\n*****\n*****\n')
    user_name = None
    check_user_name()
    while not user_name:
        user_name = input('Please enter your name: ').title()
    print('\n\tNice to meet you, ' + user_name + '!!! \n\n')
    return user_name

def read_the_rules():
    choice = input(f'Would you like to read the rules? If yes, type \'1\' and then hit Enter!\n')
    if '1' in choice:
        print('blahblahblah')
    print('\tAlrighty...\n\n\tReady?\n\tSet?!\n\tHERE WE GO!!\n\n*****\n*****')


def choose_a_task():
    choice = input(f'What action would you like to take? Type your response:\n 1: Go hangout with a customer \n 2: Take an order \n 3: Give someone the check\n')
    while choice not in ['1', '2', '3']:
        choice = input(f'\nOOPS! You entered a wrong choice. Try again:\n 1: Go hangout with a customer \n 2: Take an order \n 3: Give someone the check\n')
    return int(choice)


def check_user_name():
    user_name = None
    choice = input(f'Have you played this game before?\n 1: No \n 2: Yes\n')
    while choice not in ['1', '2']:
        choice = input(f'\nOOPS! You entered a wrong choice. Try again: \nHave you played this game before?\n 1: No \n 2: Yes\n')
    if choice == '1':
        while not user_name:
            user_name = input('Please enter your name: ').title()
        print('\n\tNice to meet you, ' + user_name + '!!! \n\n')
        with open('gameplay_records.txt', mode='a', encoding='utf-8') as gameplay_records:
            gameplay_records.write(user_name)
    


    