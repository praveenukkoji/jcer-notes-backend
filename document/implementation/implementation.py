from document.models import Documents
from restapi.connection import DBConnection
from sqlalchemy.exc import SQLAlchemyError
from document.utils import get_document_payload,  document_columns
import uuid
import os


class DocumentImplementation:
    def __init__(self, requests):
        self.requests = requests

    # create document
    def create_document(self):
        payload = []
        count = 0
        try:
            document_to_create = self.requests.get("document", None)
            with DBConnection() as session:
                for document in document_to_create:
                    _id = str(uuid.uuid4())
                    try:
                        new_document = Documents(
                            document_id=_id,
                            document_title=document['document_title'],
                            document_url=document['document_url'],
                            subject_id=document['subject_id'],
                            module=document['module']
                        )
                        session.add(new_document)
                        session.commit()
                        payload.append({"document_id": _id, "message": "Document added successfully."})
                        count += 1
                    except SQLAlchemyError as e:
                        print(e)
                        payload.append({"document_id": _id, "message": str(e._message).split(":  ")[1].split("\\")[0]})
                        session.rollback()
        except Exception as e:
            print(e)
            raise e
        finally:
            return payload, str(count) + " document created."

    # get document
    def get_document(self):
        payload = []
        count = 0
        try:
            document_to_find = self.requests.get("document", None)
            with DBConnection() as session:
                if len(document_to_find):
                    for document in document_to_find:
                        query = session.query(Documents).filter(Documents.document_id == document)
                        data = query.all()
                        if data:
                            payload1, message, count = get_document_payload(data, count)
                            payload.append(payload1[0])
                        else:
                            payload.append({"document_id": document, "message": "Document doesn't exists."})
                    message = str(count) + " document fetched."
                else:
                    query = session.query(Documents).order_by(Documents.document_title)
                    data = query.all()
                    payload, message, count = get_document_payload(data, count)
        except Exception as e:
            print(e)
            raise e
        return payload, message

    # update document
    def update_document(self):
        payload = []
        count = 0
        try:
            document_to_update = self.requests.get("document", None)
            with DBConnection() as session:
                for document in document_to_update:
                    columns_to_update = {}
                    for key, value in document["update_data"].items():
                        columns_to_update[document_columns[key]] = value

                    try:
                        query = session.query(Documents).filter(Documents.document_id == document['document_id']) \
                            .update(columns_to_update, synchronize_session=False)
                        session.commit()
                        if query:
                            count += 1
                            payload.append({"document_id": document['document_id'], "message": "Document updated successfully."})
                        else:
                            payload.append({"document_id": document['document_id'], "message": "Document doesn't exist."})

                    except SQLAlchemyError as e:
                        print(e)
                        payload.append({"document_id": document['document_id'], "message": str(e._message).split(":  ")[1].split("\\")[0]})
                        session.rollback()
        except Exception as e:
            print(e)
            raise e
        return payload, str(count) + " document updated."

    # delete document
    def delete_document(self):
        payload = []
        count = 0
        try:
            document_to_delete = self.requests.get('document', None)
            with DBConnection() as session:
                for document in document_to_delete:
                    query = session.query(Documents).filter(Documents.document_id == document)
                    data = query.all()
                    query = session.query(Documents).filter(Documents.document_id == document) \
                        .delete(synchronize_session=False)
                    if query:
                        count += 1
                        path_ = os.getcwd()+"/media/"+data[0].document_url.split("/")[4]
                        os.remove(path_)
                        payload.append({"document_id": document, "message": "Document deleted successfully."})
                        session.commit()
                    else:
                        payload.append({"document_id": document, "message": "Document doesn't exists."})
        except Exception as e:
            print(e)
            raise e
        return payload, str(count) + " document deleted."

    # get by subject_id
    def get_sub_id_document(self):
        payload = []
        count = 0
        try:
            document_to_find = self.requests.get("document", None)
            with DBConnection() as session:
                for subject in document_to_find:
                    query = session.query(Documents).filter(Documents.subject_id == subject)
                    data = query.all()
                    if data:
                        payload1, message, count = get_document_payload(data, count)
                        payload = payload1
                    else:
                        payload.append({"subject_id": subject, "message": "Document doesn't exists."})
                message = str(count) + " document fetched."
        except Exception as e:
            print(e)
            raise e
        return payload, message
