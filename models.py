from sqlalchemy import Column, String, Integer, DECIMAL, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column("id", Integer, primary_key = True, autoincrement = True)
    name = Column("name", String(25))
    email = Column("email", String(50))

    def __init__(self, name, email):
        self.name = name
        self.email = email


class Familia(Base):
    __tablename__ = "familias"

    id = Column("id", Integer, primary_key = True, autoincrement = True)
    name = Column("name", String(30))

    flowers = relationship("Flor", back_populates="family")

    def __init__(self, name):
        self.name = name


class Flor(Base):
    __tablename__ = "flores"

    id = Column("id", Integer, primary_key = True, autoincrement = True)
    name = Column("name", String(30))
    sci_name = Column("scientific_name", String(30))
    family_id = Column("family", ForeignKey("familias.id"))

    family = relationship("Familia", back_populates="flowers")

    def __init__(self, name, sci_name, family):
        self.name = name
        self.sci_name = sci_name
        self.family = family


class Compra(Base):
    __tablename__ = "compras"

    id = Column("id", Integer, primary_key = True, autoincrement = True)
    payment_method = Column("payment", String(15))
    price = Column("price", Integer)

    client = Column("client", ForeignKey("clientes.id"))
    flower = Column("flower", ForeignKey("flores.id"))

    def __init__(self, payment_method, price, client, flower):
        self.payment_method = payment_method
        self.price = price
        self.client = client
        self.flower = flower


    