from Implementation.Utils.reponses import forbidden_response, server_error_response, success_response


def delete_event(connection, cursor, user_id, event_instance_id):

    global nb_occurrence

    # voir si l'étudiant est bien inscrit à ce cours
    try:
        mysql_Query = "SELECT COUNT(*) " \
                      "FROM `assistant-etudiant`.EVENT_DATE, `assistant-etudiant`.SCHEDULE, `assistant-etudiant`.CALENDER " \
                      "WHERE EVENT_DATE.id_instance = %s AND EVENT_DATE.event_id = SCHEDULE.id AND SCHEDULE.id_course = CALENDER.id_element AND CALENDER.id_user = %s "
        cursor.execute(mysql_Query, (event_instance_id, user_id))
        nb_occurrence = cursor.fetchall()[0][0]
    except Exception as e:
        print(e)
        return server_error_response

    if nb_occurrence == 0:
        response = forbidden_response
        response["message"] = "Vous n'avez pas le droit d'effacer cet événement. Soit vous n'y êtes pas inscrit, soit cet événement n'existe pas."
        return response
    else:
        # effacer l'événement
        try:
            mysql_Query = "DELETE " \
                          "FROM `assistant-etudiant`.EVENT_DATE " \
                          "WHERE id_instance = %s"
            cursor.execute(mysql_Query, (event_instance_id,))
            val = cursor.fetchall()
            connection.commit()
            return success_response
        except Exception as e:
            print(e)
            return server_error_response



