import datetime
from datetime import datetime

from Implementation.Utils.reponses import server_error_response, success_response, not_found_response


def get_tasks(connection, cursor, student_id, task_id_, start_date, end_date):

    global data, nb_taches

    task_id = task_id_

    if task_id_ is None:
        task_id = "%"

    # obtenir les données des tâches et des cours auxquels ils sont liés
    try:
        mysql_Query = "SELECT CALENDER.*, TASKS.* " \
                      "FROM `assistant-etudiant`.TASKS ,`assistant-etudiant`.CALENDER " \
                      "WHERE TASKS.course_id = CALENDER.id_element AND CALENDER.id_user = %s AND TASKS.id LIKE %s " \
                      "ORDER BY TASKS.deadline DESC "
        cursor.execute(mysql_Query, (student_id,task_id))
        data = cursor.fetchall()

        mysql_Query = "SELECT COUNT(*) " \
                      "FROM `assistant-etudiant`.TASKS ,`assistant-etudiant`.CALENDER " \
                      "WHERE TASKS.course_id = CALENDER.id_element AND CALENDER.id_user = %s AND TASKS.id LIKE %s "
        cursor.execute(mysql_Query, (student_id, task_id))
        nb_taches = cursor.fetchall()[0][0]
    except Exception as e:
        print(e)
        return server_error_response

    if nb_taches == 0:
        return not_found_response

    response = success_response

    response["data"] = []

    # iterer sur les tâches
    for i in data:
        deadline_str = str(i[14])
        deadline = datetime.strptime(deadline_str, '%Y-%m-%d')

        if start_date is None or deadline >= start_date:
            if end_date is None or deadline <= end_date:

                to_append = {}

                to_append["task_id"] = i[11]
                to_append["type"] = i[12]
                to_append["description"] = i[13]
                to_append["deadline"] = str(i[14])
                to_append["status"] = i[15]
                to_append["course_id"] = i[16]
                to_append["assimilated"] = i[17]
                to_append["state"] = i[18]
                to_append["course_name"] = i[1]
                to_append["course_color"] = i[8]

                response["data"].append(to_append)

    return response