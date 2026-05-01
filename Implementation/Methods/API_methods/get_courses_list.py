from Implementation.Utils.reponses import server_error_response, success_response


def get_courses_list(connection, cursor, user_id):

    global data

    # obtenir les cours de l'étudiant
    try:
        mysql_Query = "SELECT * " \
                      "FROM `assistant-etudiant`.CALENDER " \
                      "WHERE id_user = %s "

        cursor.execute(mysql_Query, (user_id, ))
        data = cursor.fetchall()

    except Exception as e:
        print(e)
        return server_error_response

    response = success_response

    list = []

    # itérer sur les cours
    for i in data:
        to_append = {}
        to_append["course_id"] = i[10]
        to_append["course_name"] = i[1]
        to_append["color"] = i[8]

        list.append(to_append)

    response["data"] = list

    return response

