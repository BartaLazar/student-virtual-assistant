import uuid

from Implementation.Utils.reponses import server_error_response, bad_request_response, \
    created_response


def parse_course_event(connection, cursor, course_id, schedule_id, student_id):
    #verifier si le cours est bien dans le calendreier de l'étudiant
    mysql_Query = "SELECT COUNT(*) " \
                  "FROM CALENDER " \
                  "WHERE id_element = %s AND id_user = %s "
    cursor.execute(mysql_Query, (course_id, student_id))
    nb_cours = cursor.fetchall()[0][0]

    #si le cours est bien pris par l'étudiant, alors on peut continuer
    if nb_cours > 0:

        # créer une vue avec les dates des événements et leur type liés à ce cours
        current_view = "VIEW_TASKS_" + student_id + "__" + course_id[0:10]
        current_view = current_view.replace("-", "_")
        mysql_Query = "CREATE OR REPLACE VIEW " + current_view + " AS " \
                      "SELECT EVENT_DATE.*, SCHEDULE.type " \
                      "FROM EVENT_DATE, SCHEDULE, CALENDER " \
                      "WHERE EVENT_DATE.event_id = SCHEDULE.id AND SCHEDULE.id_course = CALENDER.id_element AND CALENDER.id_user = %s AND SCHEDULE.id = %s " \
                      "ORDER BY date "
        cursor.execute(mysql_Query, (student_id, schedule_id))
        values = cursor.fetchall()

        #choisir les lignes de la vue precedente
        mysql_Query = "SELECT type, user_id, date " \
                      "FROM " + current_view + " " \
                      "WHERE type = 'Cours' " \
                      "ORDER BY date "
        cursor.execute(mysql_Query)
        values = cursor.fetchall()

        # insérer les lignes des cours de la vue precedente dans task
        for i in values:
            try:
                mySql_Create_Table_Query = "INSERT INTO TASKS (id, type, deadline, course_id) VALUES(%s, %s, %s, %s)"
                val = (str(uuid.uuid4()), i[0], i[2], course_id)
                result = cursor.execute(mySql_Create_Table_Query, val)
                connection.commit()
            except Exception as e:
                print("La tâche " + str(i) + " n'a pas pu être ajouté")
                print(e)
                val = server_error_response
                val["message"] = ("La tâche " + str(i) + " n'a pas pu être ajouté.")
                return val

        # effacer la vue, car elle est polluante
        mysql_Query = "DROP VIEW " + current_view + " "
        cursor.execute(mysql_Query)
        values = cursor.fetchall()

        return created_response
    else:
        val = bad_request_response
        val["message"] = "Le cours n'a pas été pris par l'étudiant"
        return val

