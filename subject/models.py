from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# subject model
class Subjects(Base):
    __tablename__ = "subject"

    subject_id = Column(String, primary_key=True)
    subject_name = Column(String)
    subject_code = Column(String)
    branch_id = Column(String)
    sem = Column(Integer)
    year = Column(Integer)

    def __init__(self, subject_id, subject_name, subject_code, branch_id, sem, year):
        self.subject_id = subject_id
        self.subject_name = subject_name
        self.subject_code = subject_code
        self.branch_id = branch_id
        self.sem = sem
        self.year = year
