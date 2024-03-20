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

@app.route('/api/services', methods=['POST'])
def add_services():
    data=request.json["services"]
    sql="INSERT INTO services (name) VALUES "
    for s in data:
        sql+=f"('{s}'), "
    try:
        db.query(sql.rstrip(', '))
    except Exception as e:
        print(e)
        return json.dumps({
            "status":"problem",
            "length":-1
        })
    return json.dumps({
        "status":"ok",
        "length":len(data)
    })
    
    


if __name__ == '__main__':
    app.run(debug=True)