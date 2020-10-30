from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# document
class Documents(Base):
    __tablename__ = 'document'

    document_id = Column(String, primary_key=True)
    document_title = Column(String)
    document_url = Column(String)
    subject_id = Column(String)
    module = Column(Integer)

    def __init__(self, document_id, document_title, document_url, subject_id, module):
        self.document_id = document_id
        self.document_title = document_title
        self.document_url = document_url
        self.subject_id = subject_id
        self.module = module
