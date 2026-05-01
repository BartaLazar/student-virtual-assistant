import time

import requests
import mysql.connector # pour importer:  pip install mysql-connector-python
from mysql.connector import Error
import random

def parse_courses(connection, cursor):
    for k in range(3):
        api_result = requests.get("http://pgc.unige.ch/api/teachings/find?academicalYear=2022&page="+str(k)+"&size=5000") # effectue la rquêze

        api_response = api_result.json() # transforme le résultat de la requête en format JSON (dictionnaire clé-valeurs)


        for i in api_response['_data']:
            enitity_id_ = i["entityId"]
            id_ = i["code"]
            print("Parsing cours n°" + enitity_id_)
            further_info = "https://pgc.unige.ch/main/api/teachings/" + enitity_id_
            infos_cours = requests.get(further_info).json()

            try:
                id_ = infos_cours["entityId"]
            except:
                id_ = None
            try:
                name_ = infos_cours["title"]
            except:
                name_ = None
            try:
                description_ = infos_cours["activities"][0]["description"]
                for f in range(len(infos_cours["activities"])):
                    if infos_cours["activities"][f]["type"] == "Cours":
                        description_ = infos_cours["activities"][f]["description"]
            except:
                description_ = None
            try:
                code_ = infos_cours["code"]
            except:
                code_ = None

            color_ = "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])

            try:
                mySql_Create_Table_Query = "INSERT INTO UNIGE_COURSES (id, name, description, code, color) VALUES(%s, %s, %s, %s, %s)"
                val = (id_, name_, description_, code_, color_)
                result = cursor.execute(mySql_Create_Table_Query, val)
                connection.commit()

            except mysql.connector.errors.IntegrityError:
                print("Le cours " + id_ + " est déjà dans la BD.")


    return 0