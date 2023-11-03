from flask import Flask, jsonify
from flask_cors import CORS
from src import getData

app = Flask(__name__)
CORS(app)  

@app.route('/api/Nmembers', methods=['GET'])
def get_Nmembers():
    members = getData.getNmembers()
    return jsonify(members)

if __name__ == '__main__':
    app.run(debug=True)

    