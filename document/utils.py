from document.models import Documents
from branch.models import Branches
from subject.models import Subjects
from restapi.connection import DBConnection


def get_document_payload(data, count):
    try:
        payload = []
        for document in data:
            with DBConnection() as session:
                try:
                    query = session.query(Subjects).filter(Subjects.subject_id == document.subject_id)
                    data1 = query.all()
                    if data1:
                        for subject in data1:
                            subject_name = subject.subject_name
                            subject_code = subject.subject_code
                            sem = subject.sem
                            year = subject.year
                            branch_id = subject.branch_id
                    query1 = session.query(Branches).filter(Branches.branch_id == branch_id)
                    data2 = query1.all()
                    if data1:
                        for branch in data2:
                            branch_name = branch.branch_name
                except Exception as e:
                    print(e)
                    raise e
            new_document = {
                "document_id": document.document_id,
                "document_title": document.document_title,
                "document_url": document.document_url,
                "module": document.module,
                "branch_name": branch_name,
                "sem": sem,
                "year": year,
                "subject_name": subject_name,
                "subject_code": subject_code
            }
            payload.append(new_document)
            count += 1
    except Exception as e:
        print(e)
        raise e
    return payload, str(count) + " document fetched.", count


document_columns = {
    "document_title": Documents.document_title,
    "document_url": Documents.document_url,
    "subject_id": Documents.subject_id,
    "module": Documents.module,
}