from datetime import datetime

import flask
from flask_cors import CORS,cross_origin
import mysql
import mysql.connector
#from sshtunnel import SSHTunnelForwarder
from flask import Flask, redirect, url_for, render_template, request, flash, send_from_directory, jsonify

from Implementation.Methods.API_methods.add_course import add_course
from Implementation.Methods.API_methods.add_event import add_event_to_schedule
from Implementation.Methods.API_methods.add_holiday import add_holiday
from Implementation.Methods.API_methods.add_task import add_task
from Implementation.Methods.API_methods.course_data import get_course_data
from Implementation.Methods.API_methods.delete_course import delete_course
from Implementation.Methods.API_methods.delete_event import delete_event
from Implementation.Methods.API_methods.delete_task import delete_task
from Implementation.Methods.API_methods.get_courses_list import get_courses_list
from Implementation.Methods.API_methods.get_event_types import get_event_types
from Implementation.Methods.API_methods.get_events import get_events
from Implementation.Methods.API_methods.get_task_states import get_task_states
from Implementation.Methods.API_methods.get_task_types import get_task_types
from Implementation.Methods.API_methods.get_tasks import get_tasks
from Implementation.Methods.API_methods.get_user_infos import get_user_infos
from Implementation.Methods.API_methods.modify_event import modify_event
from Implementation.Methods.API_methods.modify_task import modify_task
from Implementation.Methods.Parsing.parse_events import find_course_id_pgc, parse_events
from Implementation.Methods.Parsing.parse_task_event import parse_course_event
from Implementation.Utils import reponses
from Implementation.Utils.debut_fin_semestre import debut_fin_semestre
from Implementation.Methods.API_methods.signup import signup
from Implementation.Methods.API_methods.connection import verify_login, disconnect, verify_if_connected
from Implementation.Utils.reponses import not_connected_response, success_response, not_found_response, \
    bad_request_response

app = Flask(__name__)
app.secret_key = "dfiefwfefneife_efwo"


CORS(app,resources={r"/api": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

def cnx():
    return mysql.connector.connect(host='localhost', database='assistant-etudiant', user='root', password='')


connection = cnx()
cursor = connection.cursor()

# très bon site sur les paramètres: https://www.educba.com/flask-url-parameters/

site = 'http://127.0.0.1:5000'




@app.route("/<id>", methods=['POST', 'GET'])
@cross_origin(origin='*',headers=['Content-Type'])
def home(id):
    id_user = str(id).replace("id=", "")
    api_to_use = site + "/" + str(id) + "/data"
    return render_template("test2.html", api=api_to_use)



# @app.route("/<id>/data",
#            methods=['POST', 'GET'])  # endpoint qui ne revoie que les données en JSON. Utilisé par le page front
# def data(id):
#     # server.start()
#     connection = cnx()
#     cursor = connection.cursor()
#     body = {}
#     # id_user = request.args.get('id')
#     id_user = str(id).replace("id=", "")
#     print(id_user)
#
#     if request.method == 'GET':
#         body = GET_names.get_names(cursor, connection)
#         body["user"] = id_user
#         response = flask.jsonify(body)
#         response.headers.add('Access-Control-Allow-Origin', '*')
#         print(response.json)
#         if connection.is_connected():
#             cursor.close()
#             connection.close()
#             # server.stop()
#         return response

@app.route("/connect/data", methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type'])
def connect():
    datab = request.get_json()
    response = jsonify(verify_login(connection, cursor, datab["email"], datab["password"]))
    #response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    # !!!! bien garder le id de l'utilisateur dans le front, car il sera utilisé,pour les reqêtes!!


@app.route("/signup/data", methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type'])
def signup_api():
    datab = request.get_json()
    print(datab)
    response = jsonify(signup(connection, cursor, datab))
    print(response)
    return response
    # !!!! bien garder le id de l'utilisateur dans le front, car il sera utilisé,pour les reqêtes!!


@app.route("/<id>/disconnect/data", methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type'])
def disconnect_api(id):
    id_user = str(id).replace("id=", "")
    response = jsonify(disconnect(connection, cursor, id_user))
    return response


@app.route("/<id>/schedule/data/pgc", methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type'])
def schedule(id):
    id_user = str(id).replace("id=", "")
    connected = verify_if_connected(connection, cursor, id_user)
    if connected:
        course_id = request.args.get('course_id')
        course_name = request.args.get('course_name')
        found_ids = find_course_id_pgc(connection, cursor, course_id, course_name)
        response = jsonify(parse_events(connection, cursor, found_ids, debut_fin_semestre))
        return response
    else:
        return jsonify(not_connected_response)


@app.route("/<id>/course/data", methods=['POST', 'GET', 'PUT', 'DELETE'])
@cross_origin(origin='*',headers=['Content-Type'])
def add_event(id):
    id_user = str(id).replace("id=", "")
    connected = verify_if_connected(connection, cursor, id_user)
    if connected:
        if request.method == 'POST':
            data = request.get_json()
            response = {"instanciate_events": {}, "instanciate_tasks": {}}
            id_cours = add_course(connection, cursor, id_user, data)["id_course_element"]  # id_element dans Calendar
            print(id_cours)
            response["instanciate_events"] = (
                add_event_to_schedule(connection, cursor, id_user, data, debut_fin_semestre,
                                      id_cours))  # instancier les événements
            if response["instanciate_events"]["status_code"] == 201:
                schedule_id = response["instanciate_events"]["schedule_id"]
                response["instanciate_tasks"] = parse_course_event(connection, cursor, id_cours ,schedule_id,
                                                                   id_user)  # instamcier les taches de type cours
            else:
                response["instanciate tasks"] = bad_request_response
            return jsonify(response)
        elif request.method == 'GET':
            course_id = (request.args.get('course'))
            if course_id is None:
                response = get_courses_list(connection, cursor, id_user)
                return jsonify(response)
                #return jsonify(bad_request_response)
            response = jsonify(get_course_data(connection, cursor, course_id, id_user))
            #response.headers.add('Access-Control-Allow-Origin', '*')
            print(course_id)
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response
        elif request.method == 'PUT':
            data = request.get_json()
            event_id = (request.args.get('event_id'))
            if event_id is None:
                return jsonify(bad_request_response)
            response = modify_event(connection, cursor, id_user, event_id, data)
            return jsonify(response)
        elif request.method == 'DELETE':
            course_id = (request.args.get('course'))
            if course_id is None:
                return jsonify(bad_request_response)
            response = jsonify(delete_course(connection, cursor, id_user, course_id))
            return response

    else:
        return jsonify(not_connected_response)


@app.route("/<id>/course/tasks/data", methods=['POST', 'PUT'])
@cross_origin(origin='*',headers=['Content-Type'])
def add_task_api(id):
    id_user = str(id).replace("id=", "")
    connected = verify_if_connected(connection, cursor, id_user)
    if connected:
        if request.method == 'POST':
            data = request.get_json()
            response = jsonify(add_task(connection, cursor, data))
            return response
        elif request.method == 'PUT':
            operation = (request.args.get('op'))
            task_id = (request.args.get('task_id'))
            data = request.get_json()
            if (task_id is None) or (operation is None):
                response = bad_request_response
                response["message"] = "No valid task_id or op"
                return jsonify(response)
            response = jsonify(modify_task(connection, cursor, id_user, task_id, data, operation))
            return response
    else:
        return jsonify(not_connected_response)



@app.route("/<id>/tasks/data", methods=['GET', 'DELETE'])
@cross_origin(origin='*',headers=['Content-Type'])
def get_task(id):
    id_user = str(id).replace("id=", "")
    connected = verify_if_connected(connection, cursor, id_user)
    if connected:
        task_id = (request.args.get('task_id'))
        if request.method == 'GET':
            start_date = (request.args.get('start'))
            if start_date is not None:
                start_date = datetime.strptime(str(start_date), '%Y-%m-%d')
            end_date = (request.args.get('end'))
            if end_date is not None:
                end_date = datetime.strptime(str(end_date), '%Y-%m-%d')
            response = jsonify(get_tasks(connection, cursor, id_user, task_id, start_date, end_date))
            return response
        elif request.method == 'DELETE':

            if task_id is None:
                response = bad_request_response
                response["message"] = "No valid task id"
                return jsonify(response)
            response = delete_task(connection, cursor, id_user, task_id)
            return jsonify(response)
    else:
        return jsonify(not_connected_response)

@app.route("/<id>/events/data", methods=['GET', 'DELETE'])
@cross_origin(origin='*',headers=['Content-Type'])
def get_event(id):
    id_user = str(id).replace("id=", "")
    connected = verify_if_connected(connection, cursor, id_user)
    if connected:
        event_instance_id = (request.args.get('event_id'))
        if request.method == 'GET':
            start_date = (request.args.get('start'))
            if start_date is not None:
                start_date = datetime.strptime(str(start_date), '%Y-%m-%d')
            end_date = (request.args.get('end'))
            if end_date is not None:
                end_date = datetime.strptime(str(end_date), '%Y-%m-%d')
            response = jsonify(get_events(connection, cursor, id_user, event_instance_id, start_date, end_date))
            return response
        elif request.method == 'DELETE':
            if event_instance_id is None:
                response = bad_request_response
                response["message"] = "No valid event instance id"
                return jsonify(response)
            response = jsonify(delete_event(connection, cursor, id_user, event_instance_id))
            return response
    else:
        return jsonify(not_connected_response)

@app.route("/<id>/events/types/data", methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type'])
def event_types(id):
    id_user = str(id).replace("id=", "")
    connected = verify_if_connected(connection, cursor, id_user)
    if connected:
        response = jsonify(get_event_types(connection, cursor))
        return response
    else:
        return jsonify(not_connected_response)

@app.route("/<id>/tasks/types/data", methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type'])
def task_types(id):
    id_user = str(id).replace("id=", "")
    connected = verify_if_connected(connection, cursor, id_user)
    if connected:
        response = jsonify(get_task_types(connection, cursor))
        return response
    else:
        return jsonify(not_connected_response)

@app.route("/<id>/tasks/states/data", methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type'])
def task_states(id):
    id_user = str(id).replace("id=", "")
    connected = verify_if_connected(connection, cursor, id_user)
    if connected:
        response = jsonify(get_task_states(connection, cursor))
        return response
    else:
        return jsonify(not_connected_response)

@app.route("/<id>/events/holiday/data", methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type'])
def holiday(id):
    id_user = str(id).replace("id=", "")
    connected = verify_if_connected(connection, cursor, id_user)
    if connected:
        data = request.get_json()
        response = jsonify(add_holiday(connection, cursor, id_user, data))
        return response
    else:
        return jsonify(not_connected_response)

@app.route("/<id>/infos/data", methods=['GET'])
@cross_origin(origin='*',headers=['Content-Type'])
def get_infos(id):
    id_user = str(id).replace("id=", "")
    connected = verify_if_connected(connection, cursor, id_user)
    if connected:
        response = jsonify(get_user_infos(connection, cursor, id_user))
        return response
    else:
        return jsonify(not_connected_response)



@app.route("/close_server")
@cross_origin(origin='*',headers=['Content-Type'])
def close():
    if connection.is_connected():
        cursor.close()
        connection.close()
        # server.stop()
        # shutdown_server()
        print("Server disconnected")
        return jsonify({"status": "Closed connection"})
