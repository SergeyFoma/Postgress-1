import psycopg2
from psycopg2 import OperationalError

#connection = None
    
connection=psycopg2.connect(
    database = 'sm_app',
    user = 'sm_app_user',
    password = '2105',
    host = '127.0.0.1',
    port = '5432'
)
cursor=connection.cursor()
update_users="""
    UPDATE users SET nationality = %s WHERE id=%s;
"""
new_nationality = 'Paragway'
id = 4
cursor.execute(update_users,(new_nationality,id))
connection.commit()
