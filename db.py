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
                # if (cur.fetchall()):
                #      return cur.fetchall()
    except Exception as e:
         print(e)

def setup():
      query("CREATE TABLE IF NOT EXISTS services (id INT PRIMARY KEY, name TEXT)")

if __name__=="__main__":
    setup()