from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import crud
import models

db = create_engine("sqlite:///floricultura.db", pool_pre_ping=True, pool_recycle=3600, connect_args={'timeout': 30})
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()
Base.metadata.create_all(bind=db)

#crud.get_all_purchases(session)
crud.create_purchase(session, "PIX", 100.10, "Angélica meu amor", "Orquidea")