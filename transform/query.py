import numpy as np
from db.models import Users


def query_to_list_of_name(query):
    result_list =[]

    try:
        for i in query:
            value = i.name
            result_list.append(value)

    except:
        pass

    return result_list


def query_to_list_of_student_all(query):
    result_list = []

    try:
        for i in query:
            list_i = []
            name: str = i.name
            record_book: str = str(i.record_book)
            list_i.append(name)
            list_i.append(record_book)

            result_list.append(list_i)

    except:
        pass

    result_list = np.array(result_list)

    return result_list

def get_user_or_None(session, login):
    try:
        user = session.query(Users).filter_by(login=login).first()
        return user

    except:
        return None
