# Student virtual assistant 

## developped by Laila Laaris and Lázár Barta
### @ Université de Genève - DISTIC
October-December 2022

### Launch the backend:
Basic requirements:<br>
- Python 3
- Flask
- MySQL

Import the database from the SQL dump provided to local and name it `assistant-etudiant`.<br>
Or you can change the connection details in `api.py`.<br>
The SQL dump is completed with the UNIGE courses of the academical year 2022-2023. If you wish to update them, erase the content of the table `UNIGE_COURSES` and execute `parse.py`.<br>
Then in the command line type:<br>
`export FLASK_APP=api.py`<br>
`flask run`<br>
if required, install the necessary frameworks and components

### Launch the frontend

## API documentation:
`Implementation/API_endpoints/endpoints.md`

## Further assistance
For further assistance don't hesitate to contact us!
- Lazar.Barta@unige.ch (backend)
- Laila.Laaris@unige.ch (frontend)
