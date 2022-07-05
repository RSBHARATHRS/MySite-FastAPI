from fastapi import FastAPI
from requests import session
from database import Base, engine, Session
from models import Bharath


app = FastAPI()
session = Session()
Base.metadata.create_all(engine)


@app.get('/')
def readRoot():
    tb = Bharath(2,'Bharath','angular',9791542199)
    session.add(tb)
    session.commit()
    return { 'message': session.commit()}


@app.get('/insert')
def readRoot():
    temp = Bharath(1,'vasanth','angular',9791542199)
    session.add(temp)
    session.commit()
    return { 'message': session.commit()}

@app.get('/bharath')
def readRoot():
    # temp = Bharath(1,'vasanth','angular',9791542199)
    temp = session.query(Bharath).filter(Bharath.id == 1).all()
    # session.commit()
    return { 'message': temp}