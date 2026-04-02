# extract data from postgres database
from connector import connect_to_postgres

def extract_data():
    conn = connect_to_postgres()
    cursor = conn.cursor()
    cursor.execute("SELECT name, phone_number, date_of_birth FROM public.users")
    return cursor.fetchall()