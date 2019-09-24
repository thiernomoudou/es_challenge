import json

from flask import Flask, request, jsonify

import pig_latin

app = Flask(__name__)

@app.route("/translate",  methods=['POST'])
def latin_pig_translator():
    english_text = json.loads(request.data)
    word_to_translate = english_text.get('sentence')
    translated = pig_latin.piglatin_tranlator(word_to_translate)
    return jsonify(translated)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
