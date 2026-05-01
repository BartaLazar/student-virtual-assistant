# ajoute un événement dans SCHEDULE pour le user. Il va ensuite instancier
import uuid
from datetime import time

from Implementation.Methods.Instaciations.instaciate_events import instanciate_event
from Implementation.Utils.reponses import server_error_response, bad_request_response, \
    created_response


def add_event_to_schedule(connection, cursor, user_id, body, debut_fin_semestre, id_cours_element):
    # id_cours_element est le id de l'élément dans CALENDAR

    response = created_response

    # voir si cet événement a déjà été ajouté
    mysql_Query = "SELECT COUNT(*) " \
                  "FROM SCHEDULE " \
                  "WHERE name = %s AND hour_start = %s AND hour_end = %s AND id_course = %s AND day = %s"
    cursor.execute(mysql_Query, (body["name"], body["beginning_time"], body["end_time"], id_cours_element, body["day"]))
    nb_events = cursor.fetchall()[0][0]

    # si cet événement n'est pas deja dans SCHEDULE, ajouter
    if nb_events == 0:

        try:
            schedule_id = str(uuid.uuid4())
            response["schedule_id"] = schedule_id
            mySql_Query = "INSERT INTO SCHEDULE (id, name, day, start_date, end_date, hour_start, hour_end, type, occurence_unique, periodicity, no_room, building, id_course) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (
            schedule_id, body["name"], body["day"], body["beginning_date"], body["end_date"], body["beginning_time"],
            body["end_time"], body["type"], body["unique_occurrence"], body["regularity"], body["room"],
            body["building"], id_cours_element)
            result = cursor.execute(mySql_Query, val)
            connection.commit()

            for h in body["teachers_full_name"]:
                try:
                    mySql_Query = "INSERT INTO SCHEDULE_PROF (schedule_id, prof_full_name) VALUES(%s, %s)"
                    result = cursor.execute(mySql_Query, (schedule_id, str(h)))
                    connection.commit()
                except Exception as e:
                    print("Le prof pour l'événement' " + schedule_id + " n'a pas pu être ajouté.")
                    print(e)
                    response = server_error_response
                    print(str(e))
                    return response

        except Exception as e:
            response = server_error_response
            print(str(e))
            return response

        instanciate_event(connection, cursor, schedule_id, body["type"], debut_fin_semestre, user_id)

        return response

    response = bad_request_response
    response["message"] = "The event has already been added"
    return response
