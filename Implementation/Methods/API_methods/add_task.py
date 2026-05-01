import uuid

from Implementation.Utils.reponses import created_response, server_error_response


def add_task(connection, cursor, body):
    course_id = body["course_id"]
    type = body["type"]
    description = body["description"]
    due_date = body["due_date"]

    id = str(uuid.uuid4())

    try:
        mySql_Create_Table_Query = "INSERT INTO TASKS (id, type, description, deadline, course_id) VALUES(%s, %s, %s, %s, %s)"
        val = (id, type, description, due_date, course_id)
        result = cursor.execute(mySql_Create_Table_Query, val)
        connection.commit()
        return created_response

    except Exception as e:
        res = server_error_response
        print(e)
        return res
