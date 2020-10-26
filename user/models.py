from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# student
class Students(Base):
    __tablename__ = 'student'

    student_id = Column(String, primary_key=True)
    name = Column(String)
    usn = Column(String)
    email = Column(String)
    password = Column(String)
    branch_id = Column(String)
    sem = Column(Integer)
    year = Column(Integer)
    created_by = Column(String)
    created_on = Column(DateTime)
    modified_by = Column(String)
    modified_on = Column(DateTime)

    def __init__(self, student_id, name, usn, email, password, branch_id, sem, year, created_by, created_on,
                 modified_by, modified_on):
        self.student_id = student_id
        self.name = name
        self.usn = usn
        self.email = email
        self.password = password
        self.branch_id = branch_id
        self.sem = sem
        self.year = year
        self.created_by = created_by
        self.created_on = created_on
        self.modified_by = modified_by
        self.modified_on = modified_on


# faculty
class Faculties(Base):
    __tablename__ = 'faculty'

    faculty_id = Column(String, primary_key=True)
    name = Column(String)
    branch_id = Column(String)
    email = Column(String)
    password = Column(String)
    created_by = Column(String)
    created_on = Column(DateTime)
    modified_by = Column(String)
    modified_on = Column(DateTime)

    def __init__(self, faculty_id, name, email, password, branch_id,
                 created_by, created_on, modified_by, modified_on):
        self.faculty_id = faculty_id
        self.name = name
        self.branch_id = branch_id
        self.email = email
        self.password = password
        self.created_by = created_by
        self.created_on = created_on
        self.modified_by = modified_by
        self.modified_on = modified_on
