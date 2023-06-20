from typing import Any
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Base is established as initial object for Person to inherit from
Base = declarative_base()

class Person(Base):
    '''
    Person Class
    '''
    __tablename__ = "people"

    ssn = Column("ssn", Integer, primary_key = True)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    gender = Column("gender", CHAR)
    age = Column("age", Integer)

    def __init__(self, ssn, first, last, gender, age):
        '''
        Constructor of object
        '''
        self.ssn = ssn
        self.firstname = first
        self.lastname = last
        self.gender = gender
        self.age = age

    # Representation of Object
    def __repr__(self):
        return f"({self.ssn}) {self.firstname} {self.lastname} ({self.gender}, {self.age})"

class Thing(Base):
    '''
    Thing Class
    '''
    __tablename__ = "things"

    tid = Column("tid", Integer, primary_key = True)
    description = Column("description", String)
    owner = Column(Integer, ForeignKey("people.ssn"))

    def __init__(self, tid, description, owner):
        '''
        Constructor of object
        '''
        self.tid = tid
        self.description = description
        self.owner = owner

    # Representation of Object
    def __repr__(self):
        return f"({self.tid}) {self.description} owned by {self.owner}"

# Establish engine and bindings
engine = create_engine("sqlite:///mydb.db", echo=True)
Base.metadata.create_all(bind=engine)

# Create Session for connection to persistent store
Session = sessionmaker(bind=engine)
session = Session()

# Create person object and store to DB
person = Person(12312, "Mike", "Smith", "m", 35)
session.add(person)
session.commit()

# Create multiple people and add them to db together
p1 = Person(31234, "Anna", "Blue", "f", 40)
p2 = Person(32423, "Bob", "Blue", "m", 35)
p3 = Person(45654, "Angela", "Cold", "f", 22)

session.add(p1)
session.add(p2)
session.add(p3)
session.commit()

# Create Things with associations and add to DB
t1 = Thing(1, "Car", p1.ssn)
t2 = Thing(2, "Laptop", p1.ssn)
t3 = Thing(3, "PS5", p2.ssn)
t4 = Thing(4, "Tool", p3.ssn)
t5 = Thing(5, "Book", p3.ssn)

session.add(t1)
session.add(t2)
session.add(t3)
session.add(t4)
session.add(t5)
session.commit()



# Read from Database
results = session.query(Person).all()
for r in results:
    print(r)

results = session.query(Person).filter(Person.lastname == "Blue")
for r in results:
    print(r)
 
results = session.query(Person).filter(Person.firstname.like("%An%"))
for r in results:
    print(r)

results = session.query(Person).filter(Person.firstname._in(["Anna", "Mike"]))
for r in results:
    print(r)

results = session.query(Person).filter(Person.firstname._in(["Anna", "Mike"]))
for r in results:
    print(r)

results = session.query(Person).filter(Person.age > 25)
for r in results:
    print(r)

# Join results
results = session.query(Thing, Person).filter(Thing.owner == Person.ssn).\
    filter(Person.firstname == "Anna").all()
for r in results:
    print(r)
