import psycopg2
from psycopg2 import OperationalError

connection = None
    
connection=psycopg2.connect(
database = 'sm_app',
user = 'sm_app_user',
password = '2105',
host = '127.0.0.1',
port = '5432'
)
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")

select_users = "SELECT * FROM users"
users = execute_read_query(connection, select_users)

for user in users:
    print(user)