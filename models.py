from sqlalchemy import Column, Integer, String, Boolean, Numeric
from database import Base


class Bharath(Base):
    __tablename__ = 'bharath'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    designation = Column(String)
    phone_no = Column(Numeric)

    def __init__(self, id, name, designation, phone_no):
        self.id = id
        self.name = name
        self.designation = designation
        self.phone_no = phone_no
