import time
import uuid

import requests
import mysql.connector  # pour importer:  pip install mysql-connector-python
from mysql.connector import Error
import random

from Implementation.Utils.reponses import not_found_response, success_response


def find_course_id_pgc(connection, cursor, id, name):
    if name is not None:
        name = name.replace("%20", " ")
    mysql_Query = "SELECT id " \
                  "FROM UNIGE_COURSES " \
                  "WHERE name = %s OR id = %s "
    cursor.execute(mysql_Query, (name, id))
    ids = cursor.fetchall()
    return ids


# prend un cours et renvoie un JSON au front contenant les infos de cet événement pour permettre la complétion automatique. Les événements seront alors dans la liste déroulante et quand l'utilisateur clique sur un des événements, ça va lui remplir les champs automatiquement
def parse_events(connection, cursor, ids_cours, debut_fin_semestres):
    #response = {"success": False, "description": None, "events": []}
    if ids_cours == []:
        response = not_found_response
        response["message"] = "No course found"
        return response
    for i in ids_cours:
        id_cours = i[0]
        print("Parsing les événements du cours n°" + id_cours)
        further_info = "https://wwwi.unige.ch/cursus/programme-des-cours/api/teachings/" + id_cours
        infos_cours = requests.get(further_info).json()

        try:
            if infos_cours['status_code'] == 404:
                continue
        except:
            response = success_response
            response["events"] = []
            for f in range(len(infos_cours["activities"])):
                for g in range(len(infos_cours["activities"][f]["courses"])):
                    to_add = {}
                    activite = infos_cours["activities"][f]
                    evenement = infos_cours["activities"][f]["courses"][g]

                    to_add["id_course"] = id_cours
                    try:
                        to_add["course_name"] = infos_cours["title"]
                    except:
                        to_add["course_name"] = None
                    try:
                        to_add["name"] = activite["title"]
                    except:
                        to_add["name"] = None
                    try:
                        to_add["day"] = evenement["day"]
                    except:
                        to_add["day"] = None

                    saison = evenement["periodicity"]
                    if saison == "Printemps" or saison == "Automne":
                        to_add["start_date"] = debut_fin_semestres[saison]["Debut"]
                        to_add["end_date"] = debut_fin_semestres[saison]["Fin"]
                    elif saison == "Annuel":
                        to_add["start_date"] = debut_fin_semestres["Automne"]["Debut"]
                        to_add["end_date"] = debut_fin_semestres["Printemps"]["Fin"]
                    else:
                        to_add["start_date"] = None
                        to_add["end_date"] = None

                    #TODO gerer les cas annuels pour ne pas avoir des cours pendant la session d'exas et les vacances
                    #DONE

                    to_add["hour_start"] = (str(evenement["startHour"]) + ":15:00")
                    to_add["hour_end"] = (str(evenement["endHour"]) + ":00:00")

                    try:
                        to_add["type"] = activite["type"]
                    except:
                        to_add["type"] = None
                    try:
                        to_add["teachers"] = []
                        for h in range(len(activite["activityTeachers"])):
                            to_add["teachers"].append((activite["activityTeachers"][h]["displayFirstName"] + " " +
                                                       activite["activityTeachers"][h]["displayLastName"]))
                    except:
                        to_add["teachers"] = []
                    to_add["occurence_unique"] = False
                    to_add["periodicity"] = 1  # chaque 1 semaine
                    try:
                        to_add["no_room"] = evenement["room"]
                    except:
                        to_add["no_room"] = None
                    try:
                        to_add["building"] = evenement["building"]
                    except:
                        to_add["building"] = None

                    response["events"].append(to_add)
            return response

                    # try:
                    #     mySql_Query = "INSERT INTO SCHEDULE (id, name, day, start_date, end_date, hour_start, hour_end, type, occurence_unique, periodicity, no_room, building, id_course) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    #     val = (str(uuid.uuid4()), name_, day_, start_date_, end_date_, start_hour_, end_hour_, type_, occurence_unique_, periodicity_, no_room_, building_, id_course_)
                    #     result = cursor.execute(mySql_Query, val)
                    #     connection.commit()
                    #
                    # except mysql.connector.errors.IntegrityError:
                    #     print("L'événement' " + id_ + " est déjà dans la BD.")
                    #
                    # for h in range(len(profs_)):
                    #     print(profs_[h])
                    #     try:
                    #         mySql_Query = "INSERT INTO SCHEDULE_PROF (schedule_id, prof_full_name) VALUES(%s, %s)"
                    #         result = cursor.execute(mySql_Query, (id_, str(profs_[h])))
                    #         connection.commit()
                    #     except Exception as e:
                    #         print("Le prof pour le cours' " + id_ + " n'a pas pu être ajouté.")
                    #         print(e)
    response = not_found_response
    return response
