from turtle import title
from sqlalchemy import Column, Integer, String, Boolean, Numeric
from database import Base


class Experience(Base):
    __tablename__ = 'experience'
    id = Column(Integer, primary_key=True)
    title = Column(String(32))
    desc = Column(String)
    designation = Column(String(32))

    def __init__(self, id, name, desc, designation):
        self.id = id
        self.title = name
        self.desc = desc
        self.designation = designation


