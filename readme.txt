First api using Python
init python virtual env from vscode commands `venv`
Install libraries in python by entering the local environment for python using `source .venv/bin/activate`
then install libraries using `pip install {library}`
`pip freeze > requirements.txt` to generate requirements file
`pip install -r requirements.txt` install requirements
leave environment using `deactivate`


run fastapi `uvicorn main:app --reload`

//Notes for self about psql
psql to start 
//setting up users
//connect with as user with all permissions
\c cookbook
"GRANT ALL ON SCHEMA public TO tester;"
//reconnect with "\c cookbook tester"


Database Schema: https://drawsql.app/teams/ben-waldman/diagrams/cookbook-schema