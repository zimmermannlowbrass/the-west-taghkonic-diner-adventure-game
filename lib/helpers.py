#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Meal, Customer, Drink

engine = create_engine("sqlite:///diner.db")
Session = sessionmaker(bind=engine)
session = Session()


def enter_name(user_name):
    while not user_name:
        user_name = input('Please enter your name: ').title()
    print('Nice to meet you, ' + user_name)
    return user_name

def customer_incoming(open_tables):
    customer = session.query(Customer).first()
    print(f'Looks like we have a customer coming! Welcome in {customer.name}! Let\'s put them at a table')
    table_location = input(f'Which table should we put them at? We have table numbers {[table for table in open_tables]} available! \n')
