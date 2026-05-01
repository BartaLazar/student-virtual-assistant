from Implementation.Utils.status_codes import status_codes

success_response = {"status_code" : 200, "description" : status_codes[200], "message" : ""}

created_response = {"status_code" : 201, "description" : status_codes[201], "message" : ""}

bad_request_response = {"status_code" : 400, "description" : status_codes[400], "message" : ""}

unauthorized_response = {"status_code" : 401, "description" : status_codes[401], "message" : "Connectez-vous pour accéder à cette resource."}

forbidden_response = {"status_code" : 403, "description" : status_codes[403], "message" : "Vous n'avez pas les droits pour accéder/modifier cette resource."}

not_found_response = {"status_code" : 404, "description" : status_codes[404], "message" : "Cette ressource n'existe pas."}

teapot_response = {"status_code" : 418, "description" : status_codes[418], "message" : "Il faudrait arrêter les bêtises"}

server_error_response = {"status_code" : 500, "description" : status_codes[500], "message" : "Une erreur est survenue. Merci de re-essayer plus tard ou contacter l'administrateur de système."}

not_connected_response = {"status_code" : 401, "description" : status_codes[401], "message" : "Connectez-vous pour accéder à cette resource."}
