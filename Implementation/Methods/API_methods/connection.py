from Implementation.Methods.Utils.utils import safe_for_injection
from Implementation.Utils.reponses import success_response, server_error_response, not_found_response, \
    bad_request_response


def verify_login(connection, cursor, email, password):
    response = {}

    if safe_for_injection(email) and  safe_for_injection(password): # pour se protéger des injections SQL
        mysql_Query = "SELECT COUNT(*) " \
                      "FROM USER " \
                      "WHERE email = %s AND password = %s "
        cursor.execute(mysql_Query, (email, password))
        nb_occurrences = cursor.fetchall()[0][0]

        if nb_occurrences == 1:
            mysql_Query = "SELECT id " \
                          "FROM USER " \
                          "WHERE email = %s AND password = %s "
            cursor.execute(mysql_Query, (email, password))
            id_user = cursor.fetchall()[0][0]

            try:
                mysql_Query = "UPDATE USER " \
                              "SET connected = 1 " \
                              "WHERE email = %s AND password = %s "
                cursor.execute(mysql_Query, (email, password))
                values = cursor.fetchall()
                connection.commit()
                response = success_response
                response["user_id"] = id_user
            except:
                response = server_error_response
                response["user_id"] = None
                response["message"] = "Something went wrong"
        else:
            response = not_found_response
            response["user_id"] = None
            response["message"] = "Could not find username and password in the database"
    else:
        response = bad_request_response
        response["user_id"] = None
        response["message"] = "Invalid word in email or password"
    return response


def disconnect(connection, cursor, id):
    response = {}
    mysql_Query = "SELECT COUNT(*) " \
                  "FROM USER " \
                  "WHERE id = %s "
    cursor.execute(mysql_Query, (id,))
    nb_occurrences = cursor.fetchall()[0][0]

    if nb_occurrences == 1:
        try:
            mysql_Query = "UPDATE USER " \
                          "SET connected = 0 " \
                          "WHERE id = %s "
            cursor.execute(mysql_Query, (id,))
            values = cursor.fetchall()
            connection.commit()
            response = success_response
        except:
            response = server_error_response
            response["message"] = "Something went wrong, could not disconnect"
    else:
        response = not_found_response
        response["message"] = "User not found"
    return response


def verify_if_connected(connection, cursor, id):
    try:
        mysql_Query = "SELECT connected " \
                      "FROM USER " \
                      "WHERE id = %s "
        cursor.execute(mysql_Query, (id,))
        connected = bool(cursor.fetchall()[0][0])
        print(connected)
    except:
        connected = False
    return connected
