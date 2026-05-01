import random
import uuid

import mysql.connector

# ajoute un cours dans CALENDAR pour le user donné si ce cours n'est pas déjà dedans
from Implementation.Utils.reponses import server_error_response, created_response, forbidden_response


def add_course(connection, cursor, user_id, body):
    response = server_error_response
    response["id_course_element"] = None

    mysql_Query = "SELECT COUNT(*) " \
                  "FROM CALENDER " \
                  "WHERE id_course = %s AND id_user = %s "
    cursor.execute(mysql_Query, (body["course_code"], user_id))
    nb_occurrences = cursor.fetchall()[0][0]

    if nb_occurrences == 0:  # si le cours ne se trouve pas dans la BD, l'ajouter et instancier
        color_ = "#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
        id_ = body["course_code"]
        element_id = str(uuid.uuid4())
        try:
            mySql_Create_Table_Query = "INSERT INTO CALENDER (id_course, name, code, color, id_user, id_element) VALUES(%s, %s, %s, %s, %s, %s)"
            val = (id_, body["name"], body["course_code"], color_, user_id, element_id)
            result = cursor.execute(mySql_Create_Table_Query, val)
            connection.commit()
            response = created_response
            response["id_course_element"] = element_id
            return response

        except Exception as e:
            response = server_error_response
            print(str(e))
            response["id_course_element"] = None
            return response
    else:
        mysql_Query = "SELECT id_element " \
                      "FROM CALENDER " \
                      "WHERE id_course = %s AND id_user = %s "
        cursor.execute(mysql_Query, (body["course_code"], user_id))
        id_course_element = cursor.fetchall()[0][0]
        response = forbidden_response
        response["id_course_element"] = id_course_element
        response["message"] = "Course already added"
        return response
