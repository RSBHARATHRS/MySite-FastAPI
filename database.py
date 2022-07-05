from requests import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('postgresql://rwkumxnd:SjTEk7aGjQVIm70GiC5LjAICQIGsceVM@jelani.db.elephantsql.com/rwkumxnd')
Session = sessionmaker(bind=engine)
Base = declarative_base()