from Implementation.Utils.reponses import forbidden_response, server_error_response, success_response


def delete_task(connection, cursor, user_id, task_id):

    global nb_occurrence

    # voir si l'étudiant est bien inscrit à ce cours
    try:
        mysql_Query = "SELECT COUNT(*) " \
                      "FROM `assistant-etudiant`.TASKS , `assistant-etudiant`.CALENDER " \
                      "WHERE TASKS.id = %s AND TASKS.course_id = CALENDER.id_element AND CALENDER.id_user = %s "
        cursor.execute(mysql_Query, (task_id, user_id))
        nb_occurrence = cursor.fetchall()[0][0]
    except Exception as e:
        print(e)
        return server_error_response

    if nb_occurrence == 0:
        response = forbidden_response
        response["message"] = "Vous n'avez pas le droit d'effacer cette tâche. Soit vous n'y êtes pas inscrit, soit cette tâche n'existe pas."
        return response
    else:
        # effacer la tâche
        try:
            mysql_Query = "DELETE " \
                          "FROM `assistant-etudiant`.TASKS " \
                          "WHERE id = %s"
            cursor.execute(mysql_Query, (task_id,))
            val = cursor.fetchall()
            connection.commit()
            return success_response
        except Exception as e:
            print(e)
            return server_error_response

