from datetime import datetime

from Implementation.Utils.reponses import bad_request_response, created_response, server_error_response


def modify_event(connection, cursor, user_id, event_instance_id, body):

    #vérifier si l'utilisateur peut modifier cet événement

    mysql_Query = "SELECT COUNT(*) " \
                  "FROM `assistant-etudiant`.EVENT_DATE, `assistant-etudiant`.SCHEDULE, `assistant-etudiant`.CALENDER " \
                  "WHERE EVENT_DATE.id_instance = %s AND EVENT_DATE.event_id = SCHEDULE.id AND SCHEDULE.id_course = CALENDER.id_element AND CALENDER.id_user = %s "
    cursor.execute(mysql_Query, (event_instance_id, user_id))
    nb_events = cursor.fetchall()[0][0]

    if nb_events == 0:
        # si l'utilisateur n'est pas lié à cet événement
        response = bad_request_response
        response["message"] = "L'utilisateur n'est pas inscrit à cet événement, peut être cet événement n'existe pas"
        return response

    # mettre à jour l'événement avec les données du body
    try:

        time_start_str = body["beginning_time"]
        time_start= datetime.strptime(time_start_str, '%H:%M:%S').time()
        time_end_str = body["end_time"]
        time_end= datetime.strptime(time_end_str, '%H:%M:%S').time()

        mysql_Query = "UPDATE EVENT_DATE " \
                      "SET date = %s, hour_start = %s, hour_end = %s, no_room = %s, building = %s " \
                      "WHERE id_instance = %s "
        cursor.execute(mysql_Query, (body["date"], time_start, time_end, body["room"], body["building"], event_instance_id))
        val = cursor.fetchall()
        connection.commit()

        response = created_response
        return response
    except Exception as e:
        response = server_error_response
        response["message"] = "L'événement " + event_instance_id + " n' pas pu être modifié. Cause:" + str(e)
        return response


