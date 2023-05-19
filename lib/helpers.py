#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Meal, Customer, Drink

import random

engine = create_engine("sqlite:///diner.db")
Session = sessionmaker(bind=engine)
session = Session()


def enter_name_ready():
    print('*****\n*****\n\nWelcome to the Taghkonic Diner Adventure Game!\n\n*****\n*****\n')
    user_name = None
    while not user_name:
        user_name = input('Please enter your name: ').title()
    print('Nice to meet you, ' + user_name + '!!! Okay, here we go!\n\n*****\n*****\n')
    # ready = input('Are you SURE ready to try the Taghkonic Diner Adventure Game?\nIf yes, type any key and then hit enter! If no, just hit enter ')
    # if not ready:
    #     exit()
    
def make_a_choice():
    choice = input(f'What action would you like to take? Type your response:\n 1: Seat a customer \n 2: Take an order \n 3: Give someone the check')
    return int(choice)

    

def customer_incoming(open_tables):
    customer = session.query(Customer).filter(Customer.id == random.randint(0,1000)).first()
    print(f'Looks like we have a customer coming! Welcome in {customer.name}! Let\'s put them at a table')
    table_location = input(f'Which table should we put them at? We have table numbers {[table for table in open_tables]} available! \n')
    return [table for table in open_tables if table != int(table_location)], customer


def take_request(seated_customers):
    customer = seated_customers[0]
    # 
    # MAKE A WAY TO CHOOSE WHICH SEATED CUSTOMER YOU WANT TO HELP
    # 
    choice = input(f'You approach the table for {customer.name}.\n to take their order: \n 1: What would you like to drink? \n 2: What would you like to eat? \n')

    if int(choice) == 1:
        drink = session.query(Drink).filter(Drink.id == customer.drink_id).first()
        print(f'{customer.name} is thirsty for a {drink.name}! Going to go grab that right now...')
        destress = customer.hunger_level
        session.query(Customer).filter(Customer.id == customer.id).update({Customer.thirst_level : 0})
        return destress, drink
    
    elif int(choice) == 2:
        meal = session.query(Meal).filter(Meal.id == customer.meal_id).first()
        print(f'{customer.name} is hungry for a {meal.name}! Going to go grab that right now...')
        destress = customer.hunger_level
        session.query(Customer).filter(Customer.id == customer.id).update({Customer.hunger_level : 0})
        return destress, meal
    
    else:
        print('You stand there awkwardly and say nothing...')
        return


def give_the_check():
    pass

