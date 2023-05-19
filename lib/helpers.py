#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Meal, Customer, Drink

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
    
    

def customer_incoming(open_tables):
    customer = session.query(Customer).first()
    print(f'Looks like we have a customer coming! Welcome in {customer.name}! Let\'s put them at a table')
    table_location = input(f'Which table should we put them at? We have table numbers {[table for table in open_tables]} available! \n')
    return [table for table in open_tables if table != int(table_location)], customer


def take_request(customer):
    choice = input(f'You approach the table for {customer.name}.\n to take their order: \n 1: What would you like to drink? \n 2: What would you like to eat? \n')
    if int(choice) == 1:
        drink = session.query(Drink).filter(Drink.id == customer.drink_id).first()
        print(f'{customer.name} is thirsty for a {drink.name}')
    elif int(choice) == 2:
        print(f'')
    else:
        print('You stand there awkwardly and say nothing...')
        return


