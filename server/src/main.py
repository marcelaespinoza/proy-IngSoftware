from flask import Flask, jsonify
from flask_cors import CORS
import getData

app = Flask(__name__)
CORS(app)  

@app.route('/api/Nmembers', methods=['GET'])
def get_Nmembers():
    members = getData.getNmembers()
    return jsonify(members)


@app.route('/api/Horarios', methods=['GET'])
def get_Horarios():
    horarios = getData.getHorarios()
    return jsonify(horarios)


@app.route('/api/Member/<code>', methods=['GET'])
def get_Member(code: str):
    member = getData.getMember(code)
    print(member)
    return jsonify(member)


@app.route('/api/Member/State/<code>/<state>', methods=['POST', 'GET'])
def update_Score_By_State(code: str, state: int):
    new_score = getData.updateScoreByState(code, state)
    print(new_score)
    return jsonify({"menssage": "Puntaje y Estado han sido actualizados correctamente"})

#########################################################################################

@app.route('/emocion/predominante', methods=['GET'])
def get_emocion_predominante():
    emocionPredominante = getData.getEmocionPredominante()
    return jsonify(emocionPredominante)


@app.route('/emociones', methods=['GET'])
def get_emociones():
    dataEmociones = getData.getEmotionPoints()
    emociones = dataEmociones.keys()
    return jsonify(list(emociones))


@app.route('/areas', methods=['GET'])
def get_areas():
    areas = getData.getAreas()
    return jsonify(list(areas))

@app.route('/mainGrafico', methods=['GET'])
def get_mainGrafico():
    diccionario = getData.getValuesMainGrafico()
    return jsonify(diccionario)    


if __name__ == '__main__':
    app.run(debug=True)

    