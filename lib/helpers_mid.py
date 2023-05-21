#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Meal, Customer, Drink

import random

from helper_helpers import (
    choose_a_table,  add_to_customer_database
)

engine = create_engine("sqlite:///diner.db")
Session = sessionmaker(bind=engine)
session = Session()

 
def customer_incoming(open_tables, seated_customers):
    if seated_customers:
        dice_roll = random.randint(0,5)
        if dice_roll == 1:
            print('\n*****\n*****\n\n\GOOD NEWS!\n\tLooks like no customers are waiting right now!!!\n*****\n*****\n\n')
            return open_tables, 0
    customer = session.query(Customer).filter(Customer.id == random.randint(0,1000)).first()
    possible_choices = [str(table) for table in open_tables]
    print(f'\n*****\nLooks like we have a customer coming! Welcome in {customer.name}! Let\'s put them at a table...\n')
    table_location = input(f'Which table should we put {customer.name} at? We have table numbers {[table for table in open_tables]} available: \n')
    while table_location not in possible_choices:
        table_location = input(f'Sorry! You entered an unavailable table! These tables {[table for table in open_tables]} are available: \n')
    customer.table = int(table_location)
    seated_customers.append(customer)
    print(f'\n*****\n\tFYI - {customer.name} will add {customer.hunger_level + customer.thirst_level} stress!\n*****\n')
    return [table for table in open_tables if table != int(table_location)], int(customer.hunger_level + customer.thirst_level)


def go_hang_out_with_a_customer(seated_customers):
    customer = choose_a_table(seated_customers)
    if not customer:
        print('\nYou arrive at an empty table and stand there in silence..........')
        return
    drink = session.query(Drink).filter(Drink.id == customer.drink_id).first()
    meal = session.query(Meal).filter(Meal.id == customer.meal_id).first()
    print(f'\n*****\n*****\n\n{customer.name} let\'s you know a little about themselves:\n\n{customer}')
    print(f'{customer.name} would like the {drink} for their drink.')
    print(f'{customer.name} would like the {meal} for their meal.')


def take_an_order(seated_customers):
    customer = choose_a_table(seated_customers)
    if not customer:
        print('\nYou arrive at an empty table and stand there in silence..........')
        return 0, 0
    
    choice = input(f'\nYou approach the table for {customer.name} to take their order: \n 1: What would you like to drink? \n 2: What would you like to eat? \n')

    if int(choice) == 1:
        if customer.thirst_level == 0:
            print(f'\n"I already have a drink, thank you!" says {customer.name}')
            return 0, None
        drink = session.query(Drink).filter(Drink.id == customer.drink_id).first()
        print(f'\n{customer.name} is thirsty for a {drink.name}! Going to go grab that right now...')
        destress = customer.hunger_level
        session.query(Customer).filter(Customer.id == customer.id).update({Customer.thirst_level : 0})
        return destress, drink
    
    elif int(choice) == 2:
        if customer.hunger_level == 0:
            print(f'\n"I already have a meal, thank you!" says {customer.name}')
            return 0, None
        meal = session.query(Meal).filter(Meal.id == customer.meal_id).first()
        print(f'\n{customer.name} is hungry for a {meal.name}! Going to go grab that right now...')
        destress = customer.hunger_level
        session.query(Customer).filter(Customer.id == customer.id).update({Customer.hunger_level : 0})
        return destress, meal
    
    else:
        print('You stand there awkwardly and say nothing...')
        return 0, 0


def give_the_check(open_tables, seated_customers):
    customer = choose_a_table(seated_customers)
    if not customer:
        print('\nYou arrive at an empty table and stand there in silence..........')
        return 0, 0
    add_to_customer_database(customer)
    earned_money = 0
    if customer.thirst_level == 0:
        drink = session.query(Drink).filter(Drink.id == customer.drink_id).first()
        earned_money += drink.cost
    if customer.hunger_level == 0:
        meal = session.query(Meal).filter(Meal.id == customer.meal_id).first()
        earned_money += meal.cost
    print(f'Congratulations! You earned ${earned_money}!')
    seated_customers.pop(seated_customers.index(customer))
    open_tables.append(customer.table)
    open_tables.sort()
    return earned_money, int(customer.hunger_level + customer.thirst_level)