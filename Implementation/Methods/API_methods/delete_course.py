from Implementation.Utils.reponses import server_error_response, forbidden_response, success_response


def delete_course(connection, cursor, student_id, course_id):

    global nb_cours

    # voir si l'étudiant est inscrit à ce cours:
    try:
        mysql_Query = "SELECT COUNT(*) " \
                      "FROM `assistant-etudiant`.CALENDER " \
                      "WHERE id_user = %s AND id_element =%s "
        cursor.execute(mysql_Query, (student_id, course_id))
        nb_cours = cursor.fetchall()[0][0]
    except Exception as e:
        print(e)
        return server_error_response

    # si l'étudiant ne l'est pas:
    if nb_cours == 0:
        response = forbidden_response
        response["message"] = "Vous n'avez pas le droit d'effacer ce cours. Soit vous n'y êtes pas inscrit, soit ce cours n'existe pas."
        return response

    # si l'étudiant l'est:
    try:
        mysql_Query = "DELETE " \
                      "FROM CALENDER " \
                      "WHERE id_element = %s "
        cursor.execute(mysql_Query, (course_id,))
        val = cursor.fetchall()
        connection.commit()
        # avec cascade comme delete rule, les dépendances seront automatiquement effacés
        return success_response
    except Exception as e:
        print(e)
        return server_error_response
