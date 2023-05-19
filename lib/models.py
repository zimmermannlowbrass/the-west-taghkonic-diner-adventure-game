from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

class Meal(Base):
    __tablename__ = 'meals'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    cost = Column(Integer())

    customers = relationship('Customer', backref=backref('meals'))

    def __repr__(self):
        return f'This is the {self.name} meal. ' + \
            f'Price : {self.cost}'
    
class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    age = Column(Integer())
    email = Column(String())
    phone = Column(String())
    hunger_level = Column(Integer())
    thirst_level = Column(Integer())

    meal_id = Column(Integer(), ForeignKey('meals.id'))
    drink_id = Column(Integer(), ForeignKey('drinks.id'))

    def __repr__(self):
        return f'Customer: {self.name} ' + \
            f'has a hunger level of {self.hunger_level}/10 ' + \
            f'and a thirst level of {self.thirst_level}/10'
    
    
class Drink(Base):
    __tablename__ = 'drinks'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    cost = Column(Integer())

    customers = relationship('Customer', backref=backref('drinks'))


    def __repr__(self):
        return f'This is the {self.name} drink. ' + \
            f'Price : {self.cost}'