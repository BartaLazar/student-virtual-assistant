from Implementation.Utils.reponses import server_error_response, success_response


def get_event_types(connection, cursor):

    global data

    try:
        mysql_Query = "SELECT * " \
                      "FROM `assistant-etudiant`.EVENT_TYPES "
        cursor.execute(mysql_Query)
        data = cursor.fetchall()
    except Exception as e:
        print(e)
        return server_error_response

    response = success_response
    response["data"] = []
    for i in data:
        response["data"].append(i[0])

    return response