# extract data from postgres database
from connector import connect_to_postgres

def extract_data():
    conn = connect_to_postgres()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM public.users")
    return cursor.fetchall()