from Implementation.Utils.reponses import success_response, server_error_response


def get_user_infos(connection, cursor, user_id):
    try:
        mysql_Query = "SELECT family_name, first_name, email, cursus " \
                      "FROM `assistant-etudiant`.USER " \
                      "WHERE id = '%s' " % (user_id)
        cursor.execute(mysql_Query)
        values = cursor.fetchall()[0]

        response = success_response
        response["nom"] = values[0]
        response["prenom"] = values[1]
        response["email"] = values[2]
        response["cursus"] = values[3]

        return response
    except Exception as e:
        print(e)
        return server_error_response