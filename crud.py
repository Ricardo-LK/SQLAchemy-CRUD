from models import *
from sqlalchemy.orm import Session

# Read
def get_all_clients(session: Session):
    clients = session.query(Cliente).all()
    return clients

def get_client_by_name(session: Session, name):
    client = session.query(Cliente).filter_by(name=name).first()
    return client

def get_client_by_id(session: Session, id):
    client = session.query(Cliente).filter_by(id=id).first()
    return client


def get_all_families(session: Session):
    families = session.query(Familia).all()
    return families

def get_family(session: Session, name):
    family = session.query(Familia).filter_by(name=name).first()
    return family


def get_all_flowers(session: Session):
    flowers = session.query(Flor).all()
    return flowers

def get_flower_by_name(session: Session, name):
    flower = session.query(Flor).filter_by(name=name).first()
    return flower

def get_flower_by_id(session: Session, id):
    flower = session.query(Flor).filter_by(id=id).first()
    return flower

# Create
def create_client(session: Session, name, email):
    client = Cliente(name=name, email=email)
    session.add(client)
    session.commit()


def create_family(session: Session, name):
    family = Familia(name=name)
    session.add(family)
    session.commit()    


def create_flower(session: Session, name, sci_name, family_name):
    flower = Flor(name=name, sci_name=sci_name, family=get_family(family_name).id)
    session.add(flower)
    session.commit()


# Update
def update_client(session: Session, client_name, name=None, email=None):
    client = get_client_by_name(session, client_name)
    if name == None:
        name = client.name
    if email == None:
        email = client.email

    client.name = name
    client.email = email

    session.commit()


def update_family(session: Session, family, name):
    family.name = name

    session.commit()

def update_flower(session: Session, flower_name, new_name=None, new_sci_name=None, new_family_name=None):
    flower = get_flower_by_name(session, flower_name)
    if new_name == None:
        new_name = flower.new_name
    if new_sci_name == None:
        new_sci_name = flower.new_sci_name
    if new_family_name == None:
        new_family_name = flower.family

    flower.name = new_name
    flower.sci_name = new_sci_name
    flower.family = new_family_name
    session.commit()


# Delete
def delete_client_by_id(session: Session, client_id):
    client = get_client_by_id(session, client_id)
    session.delete(client)
    session.commit()

def delete_client_by_name(session: Session, name):
    client = get_client_by_name(session, name)
    session.delete(client)
    session.commit()

def delete_family(session: Session, family_name):
    family = get_family(session, family_name)
    session.delete(family)
    session.commit()
    
def delete_flower(session: Session, name):
    flower = get_flower_by_name(session, name)
    session.delete(flower)
    session.commit()
