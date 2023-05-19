#!/usr/bin/env python3


def enter_name_ready():
    print('*****\n*****\n*****\n*****\n\n\n\tWELCOME TO THE WEST TAGHKONCI DINER ADVENTURE GAME!!!\n\n\n*****\n*****\n*****\n*****\n')
    user_name = None
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
    while int(choice) not in [1, 2, 3]:
        choice = input(f'\nOOPS! You entered a wrong choice. Try again:\n 1: Go hangout with a customer \n 2: Take an order \n 3: Give someone the check\n')
    return int(choice)

