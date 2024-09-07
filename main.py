from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import crud
import models

db = create_engine("sqlite:///floricultura.db", connect_args={'timeout': 30})
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()
Base.metadata.create_all(bind=db)

crud.delete_client_by_name(session, "Paulu")
