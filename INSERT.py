import psycopg2
from psycopg2 import OperationalError

def connect_db(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection=psycopg2.connect(
            database = db_name,
            user = db_user,
            password = db_password,
            host = db_host,
            port = db_port
        )
        print(f'Connection database {db_name} executed successful')
    except OperationalError as e:
        print("The error {e} ocurred")
    return connection

#Insert of table
def execute_query(connection):
    connection.autocommit=True
    cursor=connection.cursor()
    users=[
        ("James", 54, "men", "american"),
        ("Julia", 22, "women", "columbia"),
        ("Bob", 23, "men", "italia")
    ]
    user = ",".join(["%s"]*len(users))

    cursor.execute(f"INSERT INTO users(name, age, gender, nationality) VALUES {user}",users)
    print("Insert +++")

execute_query(connect_db('sm_app', 'sm_app_user', '2105', '127.0.0.1', '5432'))