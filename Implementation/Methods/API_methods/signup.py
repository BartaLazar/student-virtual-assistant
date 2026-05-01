import uuid

from Implementation.Methods.Utils.utils import safe_for_injection
from Implementation.Utils.reponses import success_response, server_error_response, forbidden_response, \
    unauthorized_response, created_response


def signup(connection, cursor, body):
    response = {}
        #{"success": False, "user_id": None, "description": None}

    email = body["email"]
    # verifier si l'utilisateur a deja un compte avec son email
    mysql_Query = "SELECT COUNT(*) " \
                  "FROM USER " \
                  "WHERE email = %s "
    cursor.execute(mysql_Query, (email,))
    nb_email = cursor.fetchall()[0][0]

    if nb_email == 0:
        if safe_for_injection(body["family_name"]) and safe_for_injection(body["first_name"]) and safe_for_injection(body["email"]) and safe_for_injection(body["password"]) and safe_for_injection(body["cursus"]):
            try:
                user_id = str(uuid.uuid4())
                mySql_Create_Table_Query = "INSERT INTO USER(id, family_name, first_name, email, password, cursus, connected) VALUES(%s, %s, %s, %s, %s, %s, %s)"
                val = (user_id, body["family_name"], body["first_name"], body["email"], body["password"], body["cursus"], 1)
                result = cursor.execute(mySql_Create_Table_Query, val)
                connection.commit()
                response = created_response
                response["user_id"] = user_id
            except Exception as e:
                response = server_error_response
                print(e)
                response["user_id"] = None
        else:
            response = forbidden_response
            response["message"] = "Invalid word found"
            response["user_id"] = None
    else:
        response = unauthorized_response
        response["message"] = "The user " + email + " already has an account."
        response["user_id"] = None

    return response
