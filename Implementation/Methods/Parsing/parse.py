import mysql.connector # pour importer:  pip install mysql-connector-python

from Implementation.Methods.API_methods.get_tasks import get_tasks
from Implementation.Methods.Parsing.parse_courses import parse_courses
from Implementation.Methods.Parsing.parse_events import parse_events, find_course_id_pgc
from Implementation.Methods.Parsing.parse_task_event import parse_course_event

from Implementation.Utils.debut_fin_semestre import debut_fin_semestre

connection = mysql.connector.connect(host='localhost', database='assistant-etudiant', user='root', password='')
cursor = connection.cursor()

parse_courses(connection, cursor)
# #
# # sélectionner tous les IDs de cours UNIGE dans la BD
# mysql_Query = "SELECT id " \
#               "FROM UNIGE_COURSES"
# cursor.execute(mysql_Query)
# id_cours = cursor.fetchall()
#
# # instancier les
# for i in id_cours:
#     parse_events(connection, cursor, i[0], debut_fin_semestre)

#parse_events(connection, cursor, "2022-D200025", debut_fin_semestre)

#instanciate_event(connection, cursor, "56758", "Cours", debut_fin_semestre, "0d3b57d6-7457-4cf9-ac43-5f8760084a2a")

#instanciate_courses(connection, cursor, "2022-D200025", debut_fin_semestre, "0d3b57d6-7457-4cf9-ac43-5f8760084a2a")

#parse_course_event(connection, cursor, "98dif7d6-7457-4cf9-ac43-5f8760039ded", "0d3b57d6-7457-4cf9-ac43-5f8760084a2a")

#get_tasks(connection, cursor, "0d3b57d6-7457-4cf9-ac43-5f8760084a2a")

#find_course_id_pgc(connection, cursor, "2-D200025", "Bases de donnée")

# try:
#     mysql_Query = "INSERT INTO `assistant-etudiant`.TEST_TABLE_2 (age, date_naissane)  VALUE (1, %s)" %('2022-01-14')
#     cursor.execute(mysql_Query)
#
#     mysql_Query = "INSERT INTO `assistant-etudiant`.TEST_TABLE (nom, prenom, age, time, date) VALUE ('a','a',1, '12:00:00', '2022-01-14') "
#     cursor.execute(mysql_Query)
#
#     connection.commit()
#
#     print("Done")
#
# except Exception as e:
#     print(e)
#     connection.rollback()



if connection.is_connected():
    cursor.close()
    connection.close()
    print("MySQL connection is closed")