from flask import Flask, request
import json
import db

app = Flask(__name__)

@app.route('/api/services', methods=['GET'])
def get_services():
    tuples=db.query("SELECT name FROM SERVICES")
    data=[t[0] for t in tuples]
    return json.dumps({
        "services":data,
        "length":len(data),
        "last_updated":"3/4/2023"
    })

""" 
from chatgpt: can you insert more than one row at once with postgres sql? if yes give an example of inserting 3 records to a table with one field called name

Yes, you can insert multiple rows at once in PostgreSQL using the `INSERT INTO` statement with a single `VALUES` clause containing multiple value sets. Here's an example inserting three records into a table with one field called `name`:

```sql
INSERT INTO your_table_name (name)
VALUES
    ('John'),
    ('Alice'),
    ('Bob');
```

This statement will insert three records into the table `your_table_name`, each with a value in the `name` field: 'John', 'Alice', and 'Bob'. 

Make sure to adjust `your_table_name` to the actual name of your table.
"""
@app.route('/api/services', methods=['POST'])
def add_services():
    data=request.json["services"]
    db.query(f"INSERT INTO services (name) VALUES {tuple(data)}")
    return json.dumps({
        "status":"ok",
        "length":len(data)
    })
    


if __name__ == '__main__':
    app.run(debug=True)