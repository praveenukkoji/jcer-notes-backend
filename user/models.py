from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# faculty model
class Faculties(Base):
    __tablename__ = 'faculty'

    faculty_id = Column(String, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    created_by = Column(String)
    created_on = Column(DateTime)
    modified_by = Column(String)
    modified_on = Column(DateTime)

    def __init__(self, faculty_id, name, email, password, created_by, created_on, modified_by, modified_on):
        self.faculty_id = faculty_id
        self.name = name
        self.email = email
        self.password = password
        self.created_by = created_by
        self.created_on = created_on
        self.modified_by = modified_by
        self.modified_on = modified_on
