from turtle import title
from sqlalchemy import Column, Integer, String, Boolean, Numeric
from database import Base


class Project(Base):
    __tablename__ = 'project'
    id = Column(Integer, primary_key=True)
    title = Column(String(32))
    desc = Column(String)

    def __init__(self, id, name, desc):
        self.id = id
        self.title = name
        self.desc = desc


