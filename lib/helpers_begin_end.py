#!/usr/bin/env python3

def enter_name_ready():
    print('*****\n*****\n*****\n*****\n\n\n\tWELCOME TO THE WEST TAGHKONCI DINER ADVENTURE GAME!!!\n\n\n*****\n*****\n*****\n*****\n')
    choice = input(f'Have you played this game before?\n 1: Yes \n 2: No\n')
    while choice not in ['1', '2']:
        choice = input(f'\nOOPS! You entered a wrong choice. Try again: \nHave you played this game before?\n 1: Yes \n 2: No\n')
    if choice == '2':
        read_rules = input(f'Would you like to read the rules?\n 1: Yes \n 2: No\n')
        while read_rules not in ['1', '2']:
            read_rules = input(f'\nOOPS! You entered a wrong choice. Try again: \nWould you like to read the rules?\n 1: Yes \n 2: No\n')
        if read_rules == '1':
            read_the_rules()
    return get_user_name()


def read_the_rules():
    print('blahblahblah')


def get_user_name():
    user_name = input('Please enter your name: ').title()
    print('\n\tNice to meet you, ' + user_name + '!!! \n\n')
    print('\tAlrighty...\n\n\tReady?\n\tSet?!\n\tHERE WE GO!!\n\n*****\n*****')
    return user_name
    

def choose_a_task():
    choice = input(f'What action would you like to take? Type your response:\n 1: Go hangout with a customer \n 2: Take an order \n 3: Give someone the check\n')
    while choice not in ['1', '2', '3']:
        choice = input(f'\nOOPS! You entered a wrong choice. Try again:\n 1: Go hangout with a customer \n 2: Take an order \n 3: Give someone the check\n')
    return int(choice)
    

def game_over(user_name, money):
    print(f'\n\n\n********** GAME OVER!!!**********\n\n\nIt looks like you made a total of ${money}\n\nBetter luck next time, {user_name}!')
    with open('highscores.txt', mode='a', encoding='utf-8') as highscores:
        highscores.write(f'Name: {user_name}\nScore: {money}')