import uuid
from datetime import datetime, date, timedelta


def instanciate_event(connection, cursor, event_id, event_type, debut_fin_semestre, student_id):
    response = {"success": False, "description": None}

    days = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

    days_dictionnary = {"Monday": "Lundi",
                        "Tuesday": "Mardi",
                        "Wednesday": "Mercredi",
                        "Thursday": "Jeudi",
                        "Friday": "Vendredi",
                        "Saturday": "Samedi",
                        "Sunday": "Dimanche"}

    mysql_Query = "SELECT day, start_date, end_date, periodicity, occurence_unique, hour_start, hour_end, no_room, building " \
                  "FROM SCHEDULE " \
                  "WHERE id = %s "
    cursor.execute(mysql_Query, (event_id,))
    values = cursor.fetchall()
    event_day = values[0][0]
    start_date_str = str(values[0][1])
    end_date_str = str(values[0][2])
    periodicity = values[0][3]
    occurrence_unique = values[0][4]
    hour_start = str(values[0][5])
    hour_end = str(values[0][6])
    room = values[0][7]
    building = values[0][8]

    start_date_day_fr = days_dictionnary[datetime.strptime(start_date_str, "%Y-%m-%d").strftime("%A")]

    start_date_day_fr_index = days.index(start_date_day_fr)
    event_day_fr_index = days.index(event_day)

    difference_start_day_event_day = (event_day_fr_index - start_date_day_fr_index) % 7

    first_event_date = datetime.strptime(start_date_str, "%Y-%m-%d") + timedelta(days=difference_start_day_event_day)

    end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

    date_to_add = first_event_date

    stop = False
    while not stop:
        instance_id = str(uuid.uuid4())
        if occurrence_unique == 1:
            try:
                mySql_Query = "INSERT INTO EVENT_DATE(id_instance, event_id, date, user_id, hour_start, hour_end, no_room, building) VALUES(%s, %s, %s, %s, %s, %s, %s, %s) "
                result = cursor.execute(mySql_Query, (
                instance_id, event_id, date_to_add.date(), student_id, hour_start, hour_end, room, building))
                connection.commit()
            except Exception as e:
                print(e)
            stop = True
        elif date_to_add > end_date:
            stop = True
        else:
            # gerer les cas des cours annuels
            if event_type in ["Cours", "Séminaire", "Expérience", "TP"] and end_date > datetime.strptime(
                    debut_fin_semestre["Automne"]["Fin"], "%Y-%m-%d") and date_to_add < datetime.strptime(
                    debut_fin_semestre["Printemps"]["Debut"], "%Y-%m-%d"):
                # le prochain jour a ajouter est le premier événement du semestre de printemps
                date_to_add = datetime.strptime(debut_fin_semestre["Printemps"]["Debut"], "%Y-%m-%d") + timedelta(days=(
                            (event_day_fr_index - (days_dictionnary[
                                datetime.strptime(debut_fin_semestre["Printemps"]["Debut"], "%Y-%m-%d").strftime(
                                    "%A")])) % 7))
                continue
            else:
                try:
                    mySql_Query = "INSERT INTO EVENT_DATE(id_instance, event_id, date, user_id, hour_start, hour_end, no_room, building) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
                    result = cursor.execute(mySql_Query, (
                    instance_id, event_id, date_to_add.date(), student_id, hour_start, hour_end, room, building))
                    connection.commit()
                except Exception as e:
                    print(e)
                date_to_add = date_to_add + timedelta(days=(periodicity * 7))

    response["success"] = True
    return response
