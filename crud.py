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


def get_all_purchases(session: Session):
    purchase = session.query(Compra).all()
    return purchase

def get_purchase(session: Session, id):
    purchase = session.query(Compra).filter_by(id=id).first()
    return purchase

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
    family = get_family(session, family_name)
    flower = Flor(name=name, sci_name=sci_name, family=family)
    session.add(flower)
    session.commit()


def create_purchase(session: Session, payment_method, price, client_name, flower_name):
    client = get_client_by_name(session, client_name).id
    flower = get_flower_by_name(session, flower_name).id
    purchase = Compra(payment_method=payment_method, price=price, client=client, flower=flower)
    session.add(purchase)
    session.commit()


# Update
def update_client(session: Session, client_name, name=None, email=None):
    client = get_client_by_name(session, client_name)
    if name != None:
        client.name = name
    if email != None:
        client.email = email

    session.commit()


def update_family(session: Session, family, name):
    family.name = name

    session.commit()

def update_flower(session: Session, flower_name, new_name=None, new_sci_name=None, new_family_name=None):
    flower = get_flower_by_name(session, flower_name)
    if new_name != None:
        flower.name = new_name
    if new_sci_name != None:
        flower.sci_name = new_sci_name
    if new_family_name != None:
        flower.family = new_family_name

    session.commit()


def update_purchase(session: Session, purchase_id, new_payment_method=None, new_price=None, new_client_name=None, new_flower_name=None):
    purchase = get_purchase(purchase_id)
    if new_payment_method != None:
        purchase.payment_method = new_payment_method
    if new_price != None:
        purchase.price = new_price
    if new_client_name != None:
        purchase.client_name = new_client_name
    if new_flower_name != None:
        purchase.flower_name = new_flower_name

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


def delete_purchase(session: Session, purchase_id):
    purchase = get_purchase(purchase_id)
    session.delete(purchase)
    session.commit()