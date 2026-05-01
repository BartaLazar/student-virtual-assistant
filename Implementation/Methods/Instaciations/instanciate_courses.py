from Implementation.Methods.Instaciations.instaciate_events import instanciate_event
from Implementation.Methods.Parsing.parse_events import parse_events


def instanciate_courses(connection, cursor, id_course, debut_fin_semestre, student_id):
    mysql_Query = "SELECT COUNT(*) " \
                  "FROM CALENDER " \
                  "WHERE id_user = %s AND id_course = %s "
    cursor.execute(mysql_Query, (student_id, id_course))
    nb_cours = cursor.fetchall()[0][0]

    # maintenant pour instancier un cours d'unige, il va instancier chaqun de ses événements. Je veux que l'instanciation se fasse par événement
    # je veux que l'utilisateur entre l'événement sur l'interface (crée un événement dans SCHEDULE et si pas necore créé, crée le cours qui va avec dans CALENDAR) et après cet élément de SCHEDULE est instancié
    parse_events(connection, cursor, id_course, debut_fin_semestre)

    # si le cours est dans le calendrier
    if nb_cours > 0:
        mysql_Query = "SELECT id, type " \
                      "FROM SCHEDULE " \
                      "WHERE id_course = %s "
        cursor.execute(mysql_Query, (id_course,))
        values = cursor.fetchall()

        for i in values:
            instanciate_event(connection, cursor, i[0], i[1], debut_fin_semestre, student_id)

