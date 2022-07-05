from fastapi import FastAPI
from requests import session
from database import Base, engine, Session
from typing import Optional
from pydantic import BaseModel


from models.bharath import Bharath
from models.project import Project
from models.experience import Experience


app = FastAPI()
session = Session()
Base.metadata.create_all(engine)


@app.get('/')
def readRoot():
    return { 'message': 'Uvicorn running'}


@app.get('/insert')
def insert():
    temp = Bharath(1,'vasanth','angular',9791542199)
    session.add(temp)
    session.commit()
    return { 'message': session.commit()}


@app.get('/bharath')
def readAll():
    temp = session.query(Bharath).filter(Bharath.id == 1).all()
    return { 'message': temp}


@app.get('/project/{id}')
def getProject(id: int):
    pro = session.query(Project).filter(Project.id == id).all()
    return { 'project': pro}