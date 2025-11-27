import psycopg2
from psycopg2 import OperationalError

connection = psycopg2.connect(
    database = 'sm_app',
    user = 'sm_app_user',
    password = '2105',
    host = '127.0.0.1',
    port = '5432'
)
cursor=connection.cursor()
delete_record = "DELETE FROM users WHERE id=%s;"
id = 2
cursor.execute(delete_record,(id,))
connection.commit()