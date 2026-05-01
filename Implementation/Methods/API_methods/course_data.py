import mysql
import mysql.connector

from Implementation.Methods.API_methods.connection import verify_if_connected
from Implementation.Methods.SQL_requests.sql_requests import sql_execute
from Implementation.Utils.reponses import not_found_response, success_response, unauthorized_response


def get_course_data(connection, cursor, course_id, student_id):

    connected = verify_if_connected(connection, cursor, student_id)

    if connected:

        response = success_response

        # voir si le cours existe:
        mysql_Query = "SELECT COUNT(*) " \
                      "FROM `assistant-etudiant`.CALENDER " \
                      "WHERE id_element = %s "
        cursor.execute(mysql_Query, (course_id,))
        nb_occurrence = cursor.fetchall()[0][0]

        # retourner erreur si non
        if nb_occurrence == 0:
            return not_found_response

        # obtenir les données du cours
        mysql_Query = "SELECT * " \
                      "FROM `assistant-etudiant`.CALENDER " \
                      "WHERE id_element = %s "
        cursor.execute(mysql_Query, (course_id,))
        values_cours = cursor.fetchall()

        print(values_cours)

        response['nom_cours'] = values_cours[0][1]
        response['color'] = values_cours[0][8]
        response['mediaserver'] = values_cours[0][4]
        response['moodle'] = values_cours[0][5]
        response['quizlet'] = values_cours[0][6]
        response['discord'] = values_cours[0][7]

        cours_id = course_id


        #recolter les infos sur les checklists
        response['checklists'] = {}
        ##recolter les infos sur les cours
        response['checklists']['courses'] = {}

        ###obtenir le nb de cours en total pour cette matière
        mysql_Query = "SELECT COUNT(*) " \
                      "FROM `assistant-etudiant`.TASKS " \
                      "WHERE type = %s AND course_id = %s "
        cursor.execute(mysql_Query, ("Cours",cours_id))
        nb_cours = cursor.fetchall()[0][0]
        response['checklists']['courses']['course_nb'] = nb_cours

        ###obtenir le nb de cours deja faits pour cette matiere
        mysql_Query = "SELECT COUNT(*) " \
                      "FROM `assistant-etudiant`.TASKS " \
                      "WHERE type = %s AND course_id = %s AND status = 1  "
        cursor.execute(mysql_Query, ("Cours", cours_id))
        nb_cours_fait = cursor.fetchall()[0][0]
        response['checklists']['courses']['course_nb_done'] = nb_cours_fait

        ###obtenir des infos sur les cours individuels
        response['checklists']['courses']['elements'] = []

        mysql_Query = "SELECT * " \
                      "FROM TASKS " \
                      "WHERE type = 'Cours' AND course_id = %s " \
                      "ORDER BY deadline "
        cursor.execute(mysql_Query, (course_id,))
        values = cursor.fetchall()

        ####mettre les infos obtenus dans elements
        order_nb = 1
        for i in values:
            to_add = {}
            to_add["element_id"] = i[0]
            to_add["order_nb"] = order_nb
            order_nb += 1
            to_add["due_date"] = str(i[3])
            to_add["description"] = i[2]
            to_add["done"] = bool(i[4])
            if i[7] == 1:
                to_add["assimilated"] = True
            else:
                to_add["assimilated"] = False
            response['checklists']['courses']['elements'].append(to_add)


        ##recolter les infos sur les tps
        response['checklists']['tps'] = {}

        ###obtenir le nb de tps en total pour cette matière
        mysql_Query = "SELECT COUNT(*) " \
                      "FROM `assistant-etudiant`.TASKS " \
                      "WHERE type = 'TP/Séminaire' AND course_id = %s "
        cursor.execute(mysql_Query, (cours_id,))
        nb_tp = cursor.fetchall()[0][0]
        response['checklists']['tps']['tp_nb'] = nb_tp

        ###obtenir le nb de tps deja faits pour cette matiere
        mysql_Query = "SELECT COUNT(*) " \
                      "FROM `assistant-etudiant`.TASKS " \
                      "WHERE type = 'TP/Séminaire' AND course_id = %s AND status = 1 "
        cursor.execute(mysql_Query, (cours_id,))
        nb_tp_fait = cursor.fetchall()[0][0]
        response['checklists']['tps']['tp_nb_done'] = nb_tp_fait

        ###obtenir des infos sur les tps individuels
        response['checklists']['tps']['elements'] = []

        mysql_Query = "SELECT * " \
                      "FROM TASKS " \
                      "WHERE type = 'TP/Séminaire' AND course_id = %s " \
                      "ORDER BY deadline "
        cursor.execute(mysql_Query, (course_id, ))
        values = cursor.fetchall()

        ####mettre les infos obtenus dans elements
        order_nb = 1
        for i in values:
            to_add = {}
            to_add["element_id"] = i[0]
            to_add["order_nb"] = order_nb
            order_nb += 1
            to_add["date"] = str(i[3])
            to_add["description"] = i[2]
            if i[4] == "Fait":
                to_add["done"] = True
            else:
                to_add["done"] = False
            response['checklists']['tps']['elements'].append(to_add)

        ##recolter les infos sur les lectures
        response['checklists']['readings'] = {}

        ###obtenir le nb de lectures en total pour cette matière
        mysql_Query = "SELECT COUNT(*) " \
                      "FROM `assistant-etudiant`.TASKS " \
                      "WHERE type = 'Lecture' AND course_id = %s "
        cursor.execute(mysql_Query, (cours_id,))
        nb_reading = cursor.fetchall()[0][0]
        response['checklists']['readings']['reading_nb'] = nb_reading

        ###obtenir le nb de lectures deja faits pour cette matiere
        mysql_Query = "SELECT COUNT(*) " \
                      "FROM `assistant-etudiant`.TASKS " \
                      "WHERE type = 'Lecture' AND course_id = %s AND status = 1  "
        cursor.execute(mysql_Query, (cours_id,))
        nb_reading_fait = cursor.fetchall()[0][0]
        response['checklists']['readings']['reading_nb_done'] = nb_reading_fait

        ###obtenir des infos sur les lectures individuels
        response['checklists']['readings']['elements'] = []

        mysql_Query = "SELECT * " \
                      "FROM TASKS " \
                      "WHERE type = 'Lecture' AND course_id = %s " \
                      "ORDER BY deadline "
        cursor.execute(mysql_Query, (course_id,))
        values = cursor.fetchall()

        ####mettre les infos obtenus dans elements
        order_nb = 1
        for i in values:
            to_add = {}
            to_add["element_id"] = i[0]
            to_add["order_nb"] = order_nb
            order_nb += 1
            to_add["due_date"] = str(i[3])
            to_add["description"] = i[2]
            to_add["done"] = bool(i[4])
            to_add["state"] = i[7]
            response['checklists']['readings']['elements'].append(to_add)

        ##recolter les infos sur les revisions
        response['checklists']['revisions'] = {}

        ###obtenir le nb revisions en total pour cette matière
        mysql_Query = "SELECT COUNT(*) " \
                      "FROM `assistant-etudiant`.TASKS " \
                      "WHERE type = 'Révision' AND course_id = %s"
        cursor.execute(mysql_Query, (cours_id,))
        nb_revision = cursor.fetchall()[0][0]
        response['checklists']['revisions']['revision_nb'] = nb_revision

        ###obtenir le nb revisions deja faits pour cette matiere
        mysql_Query = "SELECT COUNT(*) " \
                      "FROM `assistant-etudiant`.TASKS " \
                      "WHERE type = 'Révision' AND course_id = %s AND status = 1  "
        cursor.execute(mysql_Query, (cours_id,))
        nb_revision_fait = cursor.fetchall()[0][0]
        response['checklists']['revisions']['revision_nb_done'] = nb_revision_fait

        ###obtenir des infos sur lrevisions individuels
        response['checklists']['revisions']['elements'] = []

        mysql_Query = "SELECT * " \
                      "FROM TASKS " \
                      "WHERE type = 'Révision' AND course_id = %s " \
                      "ORDER BY deadline "
        cursor.execute(mysql_Query, (course_id,))
        values = cursor.fetchall()

        ####mettre les infos obtenus dans elements
        order_nb = 1
        for i in values:
            to_add = {}
            to_add["element_id"] = i[0]
            to_add["order_nb"] = order_nb
            order_nb += 1
            to_add["due_date"] = str(i[3])
            to_add["description"] = i[2]
            to_add["done"] = bool(i[4])
            to_add["state"] = i[7]
            response['checklists']['revisions']['elements'].append(to_add)

        # ajouter les données sur les séances
        response['courses'] = []

        ## récolter les types d'événements pour ce cours
        mysql_Query = "SELECT name, type, hour_start, hour_end, day, no_room, building, id_course, id " \
                      "FROM SCHEDULE " \
                      "WHERE id_course = %s "
        cursor.execute(mysql_Query, (course_id,))
        values = cursor.fetchall()

        ## itérer sur les événements de ce cours et ajouter à response
        for i in values:
            to_add = {}
            #to_add["name"] = i[0]
            to_add["type"] = i[1]
            to_add["teachers_full_name"] = []
            mysql_Query = "SELECT DISTINCT prof_full_name " \
                          "FROM SCHEDULE_PROF " \
                          "WHERE schedule_id = %s "
            cursor.execute(mysql_Query, (i[8],))
            values1 = cursor.fetchall()
            for j in values1:
                to_add["teachers_full_name"].append(j[0])
            to_add["starting_hour"] = str(i[2]).split(":")[0]
            to_add["starting_minute"] = str(i[2]).split(":")[1]
            to_add["ending_hour"] = str(i[3]).split(":")[0]
            to_add["ending_minute"] = str(i[3]).split(":")[1]
            to_add["day"] = i[4]
            to_add["room"] = str(i[6]) + " " + (i[5])
            response['courses'].append(to_add)


    else:
        response = unauthorized_response
        response["message"] = "User not connected"

    return response

    #print(response)




#connection = mysql.connector.connect(host='localhost', database='assistant-etudiant', user='root', password='')
#cursor = connection.cursor()

#get_course_data connection, cursor, '2022-D200025', '0d3b57d6-7457-4cf9-ac43-5f8760084a2a')



