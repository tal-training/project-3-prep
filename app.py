from flask import Flask, request
import json
import db

app = Flask(__name__)

@app.route('/api/services', methods=['GET'])
def get_services():
    data=db.query("SELECT name FROM SERVICES")
    return json.dumps({
        "services":data,
        "length":len(data),
        "last_updated":"3/4/2023"
    })

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