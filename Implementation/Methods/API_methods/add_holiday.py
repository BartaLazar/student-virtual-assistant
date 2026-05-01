from Implementation.Utils.reponses import server_error_response, success_response


def add_holiday(connection, cursor, student_id, body):

    global data

    # effacer les événements sauf type personnel

    ## obtenir les ids des événements à effacer
    try:
        mysql_Query = "SELECT EVENT_DATE.id_instance " \
                      "FROM `assistant-etudiant`.EVENT_DATE, `assistant-etudiant`.SCHEDULE, `assistant-etudiant`.CALENDER " \
                      "WHERE EVENT_DATE.date >= %s AND EVENT_DATE.date <= %s AND EVENT_DATE.event_id = SCHEDULE.id AND SCHEDULE.id_course = CALENDER.id_element AND CALENDER.id_user = %s AND SCHEDULE.type <> 'Personnel' "
        cursor.execute(mysql_Query, (str(body["start_date"]), str(body["end_date"]), student_id))
        data = cursor.fetchall()
    except Exception as e:
        print(e)
        return server_error_response

    ## itérer sur les ids obtenus et effacer les événements correspondants
    for i in data:
        id = i[0]
        try:
            mysql_Query = "DELETE " \
                          "FROM `assistant-etudiant`.EVENT_DATE " \
                          "WHERE id_instance = %s "
            cursor.execute(mysql_Query, (id,))
            data = cursor.fetchall()
            connection.commit()
        except Exception as e:
            print(e)
            response = server_error_response
            response["message"] = "Un événement n'a pas pu être effacé"

        # effacer les tâches de type cours et TP/Seminaire

        ## obtenir les ids des événements à effacer
        try:
            mysql_Query = "SELECT TASKS.id " \
                          "FROM `assistant-etudiant`.TASKS , `assistant-etudiant`.CALENDER " \
                          "WHERE TASKS.deadline >= %s AND TASKS.deadline <= %s AND TASKS.course_id = CALENDER.id_element AND CALENDER.id_user = %s AND (TASKS.type = 'Cours' OR TASKS.type  ='TP/Expérience') "
            cursor.execute(mysql_Query, (str(body["start_date"]), str(body["end_date"]), student_id))
            data = cursor.fetchall()
        except Exception as e:
            print(e)
            return server_error_response

        ## itérer sur les ids obtenus et effacer les tâches correspondants
        for i in data:
            id = i[0]
            try:
                mysql_Query = "DELETE " \
                              "FROM `assistant-etudiant`.TASKS " \
                              "WHERE id = %s "
                cursor.execute(mysql_Query, (id,))
                data = cursor.fetchall()
                connection.commit()
            except Exception as e:
                print(e)
                response = server_error_response
                response["message"] = "Une tâche n'a pas pu être effacé"

        # renvoyer la réponse de succes

    response = success_response
    return response

