from Implementation.Utils.reponses import server_error_response, success_response


def get_task_states(connection, cursor):

    global data

    try:
        mysql_Query = "SELECT * " \
                      "FROM `assistant-etudiant`.TASK_STATES "
        cursor.execute(mysql_Query)
        data = cursor.fetchall()
    except Exception as e:
        print(e)
        return server_error_response

    response = success_response
    response["data"] = []
    for i in data:
        response["data"].append({"state_code" : i[0], "state_name" : i[1]})

    return response