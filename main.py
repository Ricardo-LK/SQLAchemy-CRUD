from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine("sqlite:///floricultura.db", connect_args={'timeout': 30})
Session = sessionmaker(bind=db)
session = Session()



# CRUD

# Read
def get_all_clients():
    clients = session.query(Cliente).all()
    return clients

def get_client_by_name(name):
    client = session.query(Cliente).filter_by(name=name).first()
    return client

def get_client_by_id(id):
    client = session.query(Cliente).filter_by(id=id).first()
    return client


def get_all_families():
    families = session.query(Familia).all()
    return families

def get_family(name):
    family = session.query(Familia).filter_by(name=name).first()
    return family


def get_all_flowers():
    flowers = session.query(Flor).all()
    return flowers

def get_flower(name):
    flower = session.query(Flor).filter_by(name=name).first()
    return flower

# Create
def create_client(name, email):
    client = Cliente(name=name, email=email)
    session.add(client)
    session.commit()


def create_family(name):
    family = Familia(name=name)
    session.add(family)
    session.commit()    


def create_flower(name, sci_name, family_name):
    flower = Flor(name=name, sci_name=sci_name, family=get_family(family_name).id)
    session.add(flower)
    session.commit()


# Update
def update_client(client_name, name=None, email=None):
    client = get_client_by_name(client_name)
    if name == None:
        name = client.name
    if email == None:
        email = client.email

    client.name = name
    client.email = email

    session.add(client)
    session.commit()


def update_family(family, name):
    family.name = name

    session.add(family)
    session.commit()

def update_flower(flower_name, name=None, sci_name=None, family_name=None):
    flower = get_flower(flower_name)
    if name == None:
        name = flower.name
    if sci_name == None:
        sci_name = flower.sci_name
    if family_name == None:
        family_name = flower.family

    flower.name = name
    flower.sci_name = sci_name
    flower.family = family_name


# Delete
def delete_client(client_id):
    client = get_client_by_id(client_id)
    session.delete(client)
    session.commit()

def delete_family(family_name):
    family = get_family(family_name)
    session.delete(family)
    session.commit()
    
def delete_flower(name):
    flower = get_flower(name)
    session.delete(flower)
    session.commit()



Base = declarative_base()

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column("id", Integer, primary_key = True, autoincrement = True)
    name = Column("name", String)
    email = Column("email", String)

    def __init__(self, name, email):
        self.name = name
        self.email = email

class Familia(Base):
    __tablename__ = "familias"

    id = Column("id", Integer, primary_key = True, autoincrement = True)
    name = Column("name", String)

    def __init__(self, name):
        self.name = name

class Flor(Base):
    __tablename__ = "flores"

    id = Column("id", Integer, primary_key = True, autoincrement = True)
    name = Column("name", String)
    sci_name = Column("scientific_name", String)
    family = Column("family", ForeignKey("familias.id"))

    def __init__(self, name, sci_name, family):
        self.name = name
        self.sci_name = sci_name
        self.family = family




Base.metadata.create_all(bind=db)