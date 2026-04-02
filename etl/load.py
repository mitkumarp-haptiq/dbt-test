# load data to postgres database
from connector import connect_to_postgres

def load_data(data):
    conn = connect_to_postgres()
    cursor = conn.cursor()
    cursor.executemany(
        "INSERT INTO intermediate.users (name, phone_number, date_of_birth) VALUES (%s, %s, %s)",
        data,
    )
    conn.commit()
    cursor.close()
    conn.close()