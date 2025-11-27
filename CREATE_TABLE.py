import psycopg2
from psycopg2 import OperationalError

def create_connect(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print('Connection to Postgresql successful')
    except OperationalError as e:
        print(f"The error {e} eccured")
    return connection
#create_connect('sm_app', 'sm_app_user', '2105', '127.0.0.1', '5432')


#Function create table
def execute_query(connection, query):
    connection.autocommit=True
    cursor=connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successful.")
    except OperationalError as e:
        print("The error {e} occurred.")

create_user_table="""
    CREATE TABLE IF NOT EXISTS users(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    gender TEXT,
    nationality TEXT
)
"""

#create_connect('sm_app', 'sm_app_user', '2105', '127.0.0.1', '5432')
execute_query(create_connect('sm_app', 'sm_app_user', '2105', '127.0.0.1', '5432'), create_user_table)
