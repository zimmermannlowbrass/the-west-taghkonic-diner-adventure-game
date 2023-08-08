from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine




convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)

engine = create_engine("sqlite:///diner.db")
Session = sessionmaker(bind=engine)
session = Session()


class Meal(Base):
    __tablename__ = 'meals'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    cost = Column(Integer())

    customers = relationship('Customer', backref=backref('meals'))

    def __repr__(self):
        return f'{self.name} meal (price : {self.cost})'
    
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
        return f'{self.name} ' + \
            f'has a hunger level of {self.hunger_level}/10 ' + \
            f'and a thirst level of {self.thirst_level}/10'
    


    
    @classmethod
    def alphabetical(cls):
        alphabetical_data = session.query(Customer).order_by(Customer.name).all()
        return alphabetical_data
    
class Drink(Base):
    __tablename__ = 'drinks'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    cost = Column(Integer())

    customers = relationship('Customer', backref=backref('drinks'))


    def __repr__(self):
        return f'{self.name} drink (price : {self.cost})'
    


