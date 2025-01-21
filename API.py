from flask import Flask, jsonify, request
from GuessWord import GuessWord

app = Flask(__name__)
usedWord = []

@app.route('/guess', methods=['POST'])
def home():
    global usedWord
    data = request.get_json()
    if data["new"]:
        print("new")
        usedWord = []
    word = GuessWord(data["guess"],data["yellowLetters"],data["usedLetters"],usedWord)
    usedWord.append(word)
    return jsonify({"word": word})


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')