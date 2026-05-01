from Implementation.Utils.reponses import bad_request_response, created_response, server_error_response


def modify_task(connection, cursor, user_id, task_id, body, operation):
    # vérifier si l'utilisateur peut modifier cette tâche

    mysql_Query = "SELECT COUNT(*) " \
                  "FROM `assistant-etudiant`.TASKS ,`assistant-etudiant`.CALENDER " \
                  "WHERE TASKS.id = %s AND TASKS.course_id = CALENDER.id_element AND CALENDER.id_user = %s "
    cursor.execute(mysql_Query, (task_id, user_id))
    nb_events = cursor.fetchall()[0][0]

    if nb_events == 0:
        # si l'utilisateur n'est pas lié à cette tâche
        response = bad_request_response
        response["message"] = "L'utilisateur n'est pas inscrit à cette tâche, peut être cette tâche n'existe pas"
        return response

    if operation == "infos": # si on veut changer les infos de la tâche
        # mettre à jour la tâche avec les données du body
        try:

            mysql_Query = "UPDATE TASKS " \
                          "SET type = %s, description = %s, deadline = %s " \
                          "WHERE id = %s "
            cursor.execute(mysql_Query, (body["type"], body["description"], body["due_date"], task_id))
            val = cursor.fetchall()
            connection.commit()

            response = created_response
            return response
        except Exception as e:
            response = server_error_response
            response["message"] = "La tâche " + task_id + " n'a pas pu être modifié. Cause: " + str(e)
            return response

    elif operation == "status": #si on veut changer le status de la tâche
        # mettre à jour la tâche avec les données du body
        try:

            mysql_Query = "UPDATE TASKS " \
                          "SET status = %s " \
                          "WHERE id = %s "
            cursor.execute(mysql_Query, (body["status"], task_id))
            val = cursor.fetchall()
            connection.commit()

            response = created_response
            return response
        except Exception as e:
            response = server_error_response
            response["message"] = "Le status de la tâche  " + task_id + " n'a pas pu être modifié. Cause: " + str(e)
            return response

    elif operation == "state": #si on veut changer l'état de la tâche
        # mettre à jour la tâche avec les données du body
        try:

            mysql_Query = "UPDATE TASKS " \
                          "SET state = %s " \
                          "WHERE id = %s "
            cursor.execute(mysql_Query, (body["state_code"], task_id))
            val = cursor.fetchall()
            connection.commit()

            response = created_response
            return response
        except Exception as e:
            response = server_error_response
            response["message"] = "L'état de la tâche  " + task_id + " n'a pas pu être modifié. Cause: " + str(e)
            return response

    else:
        response = bad_request_response
        response["message"] = "Unknown operation for op parameter"
        return response
