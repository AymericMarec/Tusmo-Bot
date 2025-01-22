from flask import Flask, jsonify, request
from GuessWord import GuessWord
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
usedWord = []

@app.route('/guess', methods=['POST'])
def home():
    global usedWord
    data = request.get_json()
    if data["new"]:
        print("new")
        usedWord = []
    try:
        word = GuessWord(data["guess"],data["yellowLetters"],data["usedLetters"],usedWord)
        error = False
    except:
        word = ""
        error = True
    usedWord.append(word)
    return jsonify({"word": word,"error":error})


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')