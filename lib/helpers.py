#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Meal, Customer, Drink

import random

engine = create_engine("sqlite:///diner.db")
Session = sessionmaker(bind=engine)
session = Session()


def enter_name_ready():
    print('*****\n*****\n*****\n\nWELCOME TO THE WEST TAGHKONCI DINER ADVENTURE GAME!!!\n\n*****\n*****\n*****\n')
    user_name = None
    while not user_name:
        user_name = input('Please enter your name: ').title()
    print('\nNice to meet you, ' + user_name + '!!! Okay, here we go!\n\n*****\n*****')
    return user_name

    
def make_a_choice():
    choice = input(f'What action would you like to take? Type your response:\n 1: Go hangout with a customer \n 2: Take an order \n 3: Give someone the check\n')
    return int(choice)

    
def customer_incoming(open_tables):
    customer = session.query(Customer).filter(Customer.id == random.randint(0,1000)).first()
    print(f'\n*****\nLooks like we have a customer coming! Welcome in {customer.name}! Let\'s put them at a table...\n')
    table_location = input(f'Which table should we put {customer.name} at? We have table numbers {[table for table in open_tables]} available: \n')
    while int(table_location) not in open_tables:
        table_location = input(f'Sorry! You entered an unavailable table! These tables {[table for table in open_tables]} are available: \n')
    return [table for table in open_tables if table != int(table_location)], customer


def go_hang_out_with_a_customer(seated_customers):
    customer_choices = ''
    for x in range(len(seated_customers)):
        customer_choices += (str(x + 1))
        customer_choices += f'. {seated_customers[x].name} \n'
    customer_choice = input(f'\nWho would you like to take go and hang out with?\n {customer_choices}')
    customer = seated_customers[int(customer_choice) - 1]

    drink = session.query(Drink).filter(Drink.id == customer.drink_id).first()
    meal = session.query(Meal).filter(Meal.id == customer.meal_id).first()
    print(f'\n*****\n{customer.name} let\'s you know a little about themselves:\n\n{customer}')
    print(f'{customer.name} would like the {drink} for their drink.')
    print(f'{customer.name} would like the {meal} for their meal.')



def take_an_order(seated_customers):
    customer_choices = ''
    for x in range(len(seated_customers)):
        customer_choices += (str(x + 1))
        customer_choices += f'. {seated_customers[x].name} \n'
    customer_choice = input(f'\nWho would you like to take an order from?\n {customer_choices}')
    customer = seated_customers[int(customer_choice) - 1]
    
    choice = input(f'You approach the table for {customer.name} to take their order: \n 1: What would you like to drink? \n 2: What would you like to eat? \n')

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


def give_the_check(seated_customers):
    customer_choices = ''
    for x in range(len(seated_customers)):
        customer_choices += (str(x + 1))
        customer_choices += f'. {seated_customers[x].name} \n'
    customer_choice = input(f'\nWho would you like to give the check to?\n {customer_choices}')
    customer = seated_customers[int(customer_choice) - 1]

    earned_money = 0
    if customer.thirst_level == 0:
        drink = session.query(Drink).filter(Drink.id == customer.drink_id).first()
        print(drink)
        earned_money += drink.cost
    if customer.hunger_level == 0:
        meal = session.query(Meal).filter(Meal.id == customer.meal_id).first()
        print(meal)
        earned_money += meal.cost
    print(earned_money)


