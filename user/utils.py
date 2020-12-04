from user.models import Faculties


# get faculty payload
def get_faculty_payload(data, count):
    payload = []
    try:
        for faculty in data:
            new_user = {
                "faculty_id": faculty.faculty_id,
                "name": faculty.name,
                "email": faculty.email
            }
            payload.append(new_user)
            count += 1
    except Exception as e:
        print(e)
        raise e
    return payload, str(count) + " faculty fetched.", count


# columns to update
faculty_columns = {
    "name": Faculties.name,
    "email": Faculties.email,
    "password": Faculties.password
}
