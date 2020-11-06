from .models import Subjects
from restapi.connection import DBConnection
from branch.models import Branches


# get subject payload
def get_subject_payload(data, count):
    try:
        payload = []
        for subject in data:
            with DBConnection() as session:
                try:
                    query = session.query(Branches).filter(Branches.branch_id == subject.branch_id)
                    data1 = query.all()
                    if data1:
                        for branch in data1:
                            branch_name = branch.branch_name
                except Exception as e:
                    print(e)
                    raise e
            new_subject = {
                "subject_id": subject.subject_id,
                "subject_name": subject.subject_name,
                "subject_code": subject.subject_code,
                "branch_id": branch_name,
                "sem": subject.sem,
                "year": subject.year,
            }
            payload.append(new_subject)
            count += 1
    except Exception as e:
        print(e)
        raise e
    return payload, str(count) + " subject fetched.", count


# columns to update
subject_columns = {
    "subject_name": Subjects.subject_name,
    "subject_code": Subjects.subject_code,
    "branch_id": Subjects.branch_id,
    "sem": Subjects.sem,
    "year": Subjects.year
}
