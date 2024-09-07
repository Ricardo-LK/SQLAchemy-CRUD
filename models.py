from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

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

    flores = relationship("Flor", back_populates="family")

    def __init__(self, name):
        self.name = name

class Flor(Base):
    __tablename__ = "flores"

    id = Column("id", Integer, primary_key = True, autoincrement = True)
    name = Column("name", String)
    sci_name = Column("scientific_name", String)
    family_id = Column("family", ForeignKey("familias.id"))

    family = relationship("Familia", back_populates="flores")

    def __init__(self, name, sci_name, family):
        self.name = name
        self.sci_name = sci_name
        self.family = family

