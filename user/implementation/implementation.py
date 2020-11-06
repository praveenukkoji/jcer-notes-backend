from user.models import Students, Faculties
from restapi.connection import DBConnection
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
from passlib.hash import pbkdf2_sha256
from user.utils import get_student_payload, student_columns, get_faculty_payload, faculty_columns
import uuid


class UserImplementation:
    def __init__(self, requests):
        self.requests = requests

    # STUDENT

    # create students
    def create_students(self):
        payload = []
        count = 0
        try:
            students_to_create = self.requests.get("students", None)
            with DBConnection() as session:
                for student in students_to_create:
                    _id = str(uuid.uuid4())
                    try:
                        new_user = Students(
                            student_id=_id,
                            name=student['name'],
                            usn=student['usn'].lower(),
                            email=student['email'],
                            password=pbkdf2_sha256.encrypt(student['password'], rounds=1200, salt_size=32),
                            branch_id=student['branch_id'],
                            sem=student['sem'],
                            year=student['year'],
                            created_by=_id,
                            created_on=datetime.now(),
                            modified_by=_id,
                            modified_on=datetime.now(),
                        )
                        session.add(new_user)
                        session.commit()
                        payload.append({"student_id": _id, "message": "Student added successfully."})
                        count += 1
                    except SQLAlchemyError as e:
                        print(e)
                        payload.append({"student_id": _id, "message": str(e._message).split(":  ")[1].split('\\')[0]})
                        session.rollback()
        except Exception as e:
            print(e)
            raise e
        finally:
            return payload, str(count) + " student created."

    # get students
    def get_students(self):
        payload = []
        count = 0
        message = ""
        try:
            students_to_find = self.requests.get("students", None)
            with DBConnection() as session:
                if len(students_to_find):
                    for student in students_to_find:
                        query = session.query(Students).filter(Students.student_id == student)
                        data = query.all()
                        if data:
                            payload1, message, count = get_student_payload(data, count)
                            payload.append(payload1[0])
                        else:
                            payload.append({"student_id": student, "message": "Student doesn't exists."})
                else:
                    query = session.query(Students)
                    data = query.all()
                    payload, message, count = get_student_payload(data, count)
        except Exception as e:
            print(e)
            raise e
        return payload, message

    # update students
    def update_students(self):
        payload = []
        count = 0
        try:
            students_to_update = self.requests.get("students", None)
            with DBConnection() as session:
                for student in students_to_update:
                    columns_to_update = {}
                    for key, value in student["update_data"].items():
                        if key == "password":
                            value = pbkdf2_sha256.encrypt(value, rounds=1200, salt_size=32)
                            columns_to_update[student_columns[key]] = value
                        columns_to_update[student_columns[key]] = value
                    columns_to_update[Students.modified_by] = student['student_id']
                    columns_to_update[Students.modified_on] = datetime.now()

                    try:
                        query = session.query(Students).filter(Students.student_id == student['student_id']) \
                            .update(columns_to_update, synchronize_session=False)
                        session.commit()
                        if query:
                            count += 1
                            payload.append({"student_id": student['student_id'], "message": "Student updated successfully."})
                        else:
                            payload.append({"student_id": student['student_id'], "message": "Student doesn't exist."})

                    except SQLAlchemyError as e:
                        print(e)
                        payload.append({"student_id": student['student_id'],
                                        "message": str(e._message).split(":  ")[1].split("\\")[0]})
                        session.rollback()
        except Exception as e:
            print(e)
            raise e
        return payload, str(count) + " student updated."

    # delete students
    def delete_students(self):
        payload = []
        count = 0
        try:
            students_to_delete = self.requests.get('students', None)
            with DBConnection() as session:
                for student in students_to_delete:
                    query = session.query(Students.student_id).filter(Students.student_id == student) \
                        .delete(synchronize_session=False)
                    if query:
                        count += 1
                        payload.append({"student_id": student, "message": "Student deleted successfully."})
                        session.commit()
                    else:
                        payload.append({"student_id": student, "message": "Student doesn't exists."})
        except Exception as e:
            print(e)
            raise e
        return payload, str(count) + " student deleted."

    # login student
    def login_student(self):
        payload = []
        message = ""
        student = self.requests.get("student", None)
        try :
            with DBConnection() as session:
                try:
                    query = session.query(Students.student_id, Students.usn, Students.password) \
                        .filter(Students.usn == student[0]["usn"].lower())
                    data = query.all()
                    if data:
                        if pbkdf2_sha256.verify(student[0]["password"], data[0][2]):
                            payload.append({"student_id": data[0][0]})
                            message = "Logged in successfully."
                except Exception as e:
                    print(e)
                    raise e
        except Exception as e:
            print(e)
            raise e
        return payload, message

    # FACULTY

    # create faculties
    def create_faculties(self):
        payload = []
        count = 0
        try:
            faculties_to_create = self.requests.get("faculties", None)
            with DBConnection() as session:
                for faculty in faculties_to_create:
                    _id = str(uuid.uuid4())
                    try:
                        new_user = Faculties(
                            faculty_id=_id,
                            name=faculty['name'],
                            email=faculty['email'],
                            password=pbkdf2_sha256.encrypt(faculty['password'], rounds=1200, salt_size=32),
                            branch_id=faculty['branch_id'],
                            created_by=_id,
                            created_on=datetime.now(),
                            modified_by=_id,
                            modified_on=datetime.now(),
                        )
                        session.add(new_user)
                        session.commit()
                        payload.append({"faculty_id": _id, "message": "Faculty added successfully."})
                        count += 1
                    except SQLAlchemyError as e:
                        print(e)
                        payload.append({"faculty_id": _id, "message": str(e._message).split(":  ")[1].split('\\')[0]})
                        session.rollback()
        except Exception as e:
            print(e)
            raise e
        finally:
            return payload, str(count) + " faculty created."

    # get faculties
    def get_faculties(self):
        payload = []
        count = 0
        message = ""
        try:
            faculties_to_find = self.requests.get("faculties", None)
            with DBConnection() as session:
                if len(faculties_to_find):
                    for faculty in faculties_to_find:
                        query = session.query(Faculties).filter(Faculties.faculty_id == faculty)
                        data = query.all()
                        if data:
                            payload1, message, count = get_faculty_payload(data, count)
                            payload.append(payload1[0])
                        else:
                            payload.append({"faculty_id": faculty, "message": "Faculty doesn't exists."})
                else:
                    query = session.query(Faculties)
                    data = query.all()
                    payload, message, count = get_faculty_payload(data, count)
        except Exception as e:
            print(e)
            raise e
        return payload, message

    # update faculties
    def update_faculties(self):
        payload = []
        count = 0
        try:
            faculties_to_update = self.requests.get("faculties", None)
            with DBConnection() as session:
                for faculty in faculties_to_update:
                    columns_to_update = {}
                    for key, value in faculty["update_data"].items():
                        if key == "password":
                            value = pbkdf2_sha256.encrypt(value, rounds=1200, salt_size=32)
                            columns_to_update[faculty_columns[key]] = value
                        columns_to_update[faculty_columns[key]] = value
                    columns_to_update[Faculties.modified_by] = faculty['faculty_id']
                    columns_to_update[Faculties.modified_on] = datetime.now()

                    try:
                        query = session.query(Faculties).filter(Faculties.faculty_id == faculty['faculty_id']) \
                            .update(columns_to_update, synchronize_session=False)
                        session.commit()
                        if query:
                            count += 1
                            payload.append({"faculty_id": faculty['faculty_id'],
                                            "message": "Faculty updated successfully."})
                        else:
                            payload.append({"faculty_id": faculty['faculty_id'], "message": "Faculty doesn't exist."})

                    except SQLAlchemyError as e:
                        print(e)
                        payload.append({"faculty_id": faculty['faculty_id'],
                                        "message": str(e._message).split(":  ")[1].split("\\")[0]})
                        session.rollback()
        except Exception as e:
            print(e)
            raise e
        return payload, str(count) + " faculty updated."

    # delete faculties
    def delete_faculties(self):
        payload = []
        count = 0
        try:
            faculties_to_delete = self.requests.get('faculties', None)
            with DBConnection() as session:
                for faculty in faculties_to_delete:
                    query = session.query(Faculties.faculty_id).filter(Faculties.faculty_id == faculty) \
                        .delete(synchronize_session=False)
                    if query:
                        count += 1
                        payload.append({"faculty_id": faculty, "message": "Faculty deleted successfully."})
                        session.commit()
                    else:
                        payload.append({"faculty_id": faculty, "message": "Faculty doesn't exists."})
        except Exception as e:
            print(e)
            raise e
        return payload, str(count) + " faculty deleted."

    # login faculties
    def login_faculty(self):
        payload = []
        message = ""
        faculty = self.requests.get("faculty", None)
        try:
            with DBConnection() as session:
                try:
                    query = session.query(Faculties.faculty_id, Faculties.email, Faculties.password) \
                        .filter(Faculties.email == faculty[0]["email"])
                    data = query.all()
                    if data:
                        if pbkdf2_sha256.verify(faculty[0]["password"], data[0][2]):
                            payload.append({"faculty_id": data[0][0]})
                            message = "Logged in successfully."
                except Exception as e:
                    print(e)
                    raise e
        except Exception as e:
            print(e)
            raise e
        return payload, message
