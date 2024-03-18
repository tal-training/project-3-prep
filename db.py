import psycopg2

def query(sql):
    try:
        with psycopg2.connect(
            database="postgres",
            host="localhost",
            user="postgres",
            password="postgres",
            port="5432") as conn:
                cur=conn.cursor()
                cur.execute(sql)
                try:
                    return cur.fetchall()
                except Exception as e:
                     print(e)
                     
    except Exception as e:
         print(e)

"""
From chatgpt: does psychpg2 cursor execute have an option to return query result as a list of dictionaries?

import psycopg2
from psycopg2 import extras

# Connect to your database
conn = psycopg2.connect(
    dbname="your_database",
    user="your_username",
    password="your_password",
    host="your_host",
    port="your_port"
)

# Create a cursor using DictCursor
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

# Execute your query
cur.execute("SELECT * FROM your_table")

# Fetch all rows as a list of dictionaries
rows = cur.fetchall()

# Iterate over the list of dictionaries
for row in rows:
    print(row)

# Close the cursor and connection
cur.close()
conn.close()

"""


def setup():
      query("CREATE TABLE IF NOT EXISTS services (id serial PRIMARY KEY, name TEXT)")

if __name__=="__main__":
    setup()