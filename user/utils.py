from user.models import Students
from branch.models import Branches
from restapi.connection import DBConnection


# get user payload
def get_student_payload(data, count):
    payload = []
    try:
        for student in data:
            with DBConnection() as session:
                try:
                    query = session.query(Branches).filter(Branches.branch_id == student.branch_id)
                    data1 = query.all()
                    if data1:
                        for branch in data1:
                            branch_name = branch.branch_name
                except Exception as e:
                    print(e)
                    raise e
            new_user = {
                "student_id": student.student_id,
                "name": student.name,
                "usn": student.usn,
                "email": student.email,
                "branch_name": branch_name,
                "sem": student.sem,
                "year": student.year
            }
            payload.append(new_user)
            count += 1
    except Exception as e:
        print(e)
        raise e
    return payload, str(count) + " student fetched.", count


# columns to update
student_columns = {
    "name": Students.name,
    "usn": Students.usn,
    "email": Students.email,
    "password": Students.password,
    "branch_id": Students.branch_id,
    "sem": Students.sem,
    "year": Students.year,
}
