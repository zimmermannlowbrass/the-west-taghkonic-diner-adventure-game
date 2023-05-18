#!/usr/bin/env python3

import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Meal, Customer, Drink

from faker import Faker 
fake = Faker()

if __name__ == '__main__':
    engine = create_engine("sqlite:///diner.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Meal).delete()
    session.query(Customer).delete()
    session.query(Drink).delete()
    session.commit()

    meals = [
        Meal(
            name = fake.word(),
            cost = random.randint(1, 20)
        )
    for i in range(50)]

    customers = [
        Customer(
            name = fake.name(),
            age = random.randint(1,100),
            email = fake.company_email(),
            phone = fake.phone_number(),
            hunger_level = random.randint(1,10)
        )
    for i in range(1000)]

    drinks = [
        Drink(
            name = fake.word(),
            cost = random.randint(1,5)
        )
    for i in range(20)]

    session.add_all(meals)
    session.add_all(customers)
    session.add_all(drinks)
    session.commit()