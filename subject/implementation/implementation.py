from subject.models import Subjects
from restapi.connection import DBConnection
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
import uuid
from subject.utils import get_subject_payload, subject_columns


class SubjectImplementation:
    def __init__(self, requests):
        self.requests = requests

    # create subjects
    def create_subjects(self):
        payload = []
        count = 0
        try:
            subjects_to_create = self.requests.get("subjects", None)
            with DBConnection() as session:
                for subject in subjects_to_create:
                    _id = str(uuid.uuid4())
                    try:
                        new_subject = Subjects(
                            subject_id=_id,
                            subject_name=subject['subject_name'],
                            subject_code=subject['subject_code'].lower(),
                            sem=subject['sem'],
                            year=subject['year'],
                            branch_id=subject['branch_id']
                        )
                        session.add(new_subject)
                        session.commit()
                        payload.append({"subject_id": _id, "message": "Subject added successfully."})
                        count += 1
                    except SQLAlchemyError as e:
                        print(e)
                        payload.append({"subject_id": _id, "message": str(e._message).split(":  ")[1].split("\\")[0]})
                        session.rollback()
        except Exception as e:
            print(e)
            raise e
        finally:
            return payload, str(count) + " subjects created."

    # get subjects
    def get_subjects(self):
        payload = []
        count = 0
        try:
            subjects_to_find = self.requests.get("subjects", None)
            with DBConnection() as session:
                if len(subjects_to_find):
                    for subject in subjects_to_find:
                        query = session.query(Subjects).filter(Subjects.subject_id == subject)
                        data = query.all()
                        if data:
                            payload1, message, count = get_subject_payload(data, count)
                            payload.append(payload1[0])
                        else:
                            payload.append({"subject_id": subject, "message": "Subject doesn't exists."})
                    message = str(count) + " subjects fetched."
                else:
                    query = session.query(Subjects)
                    data = query.all()
                    payload, message, count = get_subject_payload(data, count)
        except Exception as e:
            print(e)
            raise e
        return payload, message

    # update subjects
    def update_subjects(self):
        payload =[]
        count = 0
        try:
            subjects_to_update = self.requests.get("subjects", None)
            with DBConnection() as session:
                for subject in subjects_to_update:
                    columns_to_update = {}
                    for key, value in subject["update_data"].items():
                        if key == 'subject_code':
                            val = value.lower()
                            columns_to_update[subject_columns[key]] = val
                        else:
                            columns_to_update[subject_columns[key]] = value
                    try:
                        query = session.query(Subjects).filter(Subjects.subject_id == subject['subject_id']) \
                            .update(columns_to_update, synchronize_session=False)
                        session.commit()
                        if query:
                            count += 1
                            payload.append({"subject_id": subject['subject_id'], "message": "Subject updated successfully."})
                        else:
                            payload.append({"subject_id": subject['subject_id'], "message": "Subject doesn't exist."})

                    except SQLAlchemyError as e:
                        print(e)
                        payload.append({"subject_id": subject['subject_id'],
                                        "message": str(e._message).split(":  ")[1].split("\\")[0]})
                        session.rollback()
        except Exception as e:
            print(e)
            raise e
        return payload, str(count) + " subject updated."

    # delete subjects
    def delete_subjects(self):
        payload = []
        count = 0
        try:
            subjects_to_delete = self.requests.get("subjects", None)
            with DBConnection() as session:
                for subject in subjects_to_delete:
                    query = session.query(Subjects).filter(Subjects.subject_id == subject).delete(synchronize_session=False)
                    if query:
                        count += 1
                        payload.append({"subject_id": subject, "message": "Subject deleted successfully."})
                        session.commit()
                    else:
                        payload.append({"subject_id": subject, "message": "Subject doesn't exists."})
        except Exception as e:
            print(e)
            raise e
        return payload, str(count) + " subject deleted."
