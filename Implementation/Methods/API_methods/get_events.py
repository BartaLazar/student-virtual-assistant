from datetime import datetime

from Implementation.Utils.reponses import server_error_response, success_response, not_found_response


def get_events(connection, cursor, student_id, event_id_, start_date, end_date):

    global data, teachers, nb_teachers, nb_events

    event_id = event_id_

    if event_id_ is None:
        event_id = "%"

    # obtenir les données des événements et des cours auxquels ils sont liés
    try:
        mysql_Query = "SELECT CALENDER.*, SCHEDULE.type, EVENT_DATE.* " \
                      "FROM `assistant-etudiant`.EVENT_DATE ,`assistant-etudiant`.SCHEDULE ,`assistant-etudiant`.CALENDER " \
                      "WHERE EVENT_DATE.event_id = SCHEDULE.id AND SCHEDULE.id_course = CALENDER.id_element AND CALENDER.id_user = %s AND EVENT_DATE.id_instance LIKE %s " \
                      "ORDER BY EVENT_DATE.date, EVENT_DATE.hour_start "
        cursor.execute(mysql_Query, (student_id, event_id))
        data = cursor.fetchall()

        mysql_Query = "SELECT COUNT(*) " \
                      "FROM `assistant-etudiant`.EVENT_DATE ,`assistant-etudiant`.SCHEDULE ,`assistant-etudiant`.CALENDER " \
                      "WHERE EVENT_DATE.event_id = SCHEDULE.id AND SCHEDULE.id_course = CALENDER.id_element AND CALENDER.id_user = %s AND EVENT_DATE.id_instance LIKE %s "
        cursor.execute(mysql_Query, (student_id, event_id))
        nb_events = cursor.fetchall()[0][0]
    except Exception as e:
        print(e)
        return server_error_response

    if nb_events == 0:
        return not_found_response

    response = success_response

    response["data"] = []

    # iterer sur les événements
    for i in data:
        date_str = str(i[14])
        date = datetime.strptime(date_str, '%Y-%m-%d')

        if start_date is None or date >= start_date:
            if end_date is None or date <= end_date:
                to_append = {}

                to_append["course_id"] = i[10]
                to_append["schedule_id"] = i[13]
                to_append["instance_id"] = i[12]
                to_append["course_name"] = i[1]
                to_append["event_type"] = i[11]
                to_append["date"] = str(i[14])
                to_append["hour_start"] = str(i[16])
                to_append["hour_end"] = str(i[17])
                to_append["no_room"] = i[18]
                to_append["building"] = i[19]
                to_append["color"] = i[8]
                to_append["teachers_full_name"] = []

                # compter le nb de profs obtenus:
                try:
                    mysql_Query = "SELECT COUNT(*) " \
                                  "FROM `assistant-etudiant`.SCHEDULE_PROF " \
                                  "WHERE SCHEDULE_PROF.schedule_id = %s "
                    cursor.execute(mysql_Query, (i[13],))
                    nb_teachers = cursor.fetchall()[0][0]
                except Exception as e:
                    print(e)
                    return server_error_response

                if nb_teachers > 0:
                    # obtenir les profs de cet événement
                    try:
                        mysql_Query = "SELECT  SCHEDULE_PROF.prof_full_name " \
                                      "FROM `assistant-etudiant`.SCHEDULE_PROF " \
                                      "WHERE SCHEDULE_PROF.schedule_id = %s "
                        cursor.execute(mysql_Query, (i[13], ))
                        teachers = cursor.fetchall()
                    except Exception as e:
                        print(e)
                        return server_error_response

                    #itérer sur les profs
                    for j in teachers:
                        to_append["teachers_full_name"].append(j[0])

                response["data"].append(to_append)

    return response