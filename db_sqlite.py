import sqlite3

def query(sql):
    try:
        with sqlite3.connect("lawyer.db") as conn:
                cur=conn.cursor()
                cur.execute(sql)
                try:
                    return cur.fetchall()
                except Exception as e:
                     print(e)
                     
    except Exception as e:
         print(e)

def setup():
      query("CREATE TABLE IF NOT EXISTS services (id PRIMARY KEY, name TEXT)")

if __name__=="__main__":
    setup()