from flask import Flask, jsonify, request
app = Flask(__name__)
heart = [

    {
        "heart_id" : "0",
        "heart_rate" : "172 bpm",
        "date" : "September 30, 2022"
    },

    {
        "heart_id" : "1",
        "heart_rate" : "210 bpm",
        "date" : "October 1, 2022"
    }
]
@app.route ('/heart', methods=['GET'])
def getHeartInfo():
    return jsonify(heart)

@app.route('/heart', methods=['POST'])
def addHeartInfo():
    heart = request.get_json()
    heart.append(heart)
    return {'id': len(heart)},200

@app.route('/heart/<int:index>', methods=['DELETE'])
def deleteHeartInfo(index):
    heart.pop(index)
    return 'Medical information was successfully deleted', 200

if __name__ == '__main__':
    app.run()