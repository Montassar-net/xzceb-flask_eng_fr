from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
     #i have renamed the method after pylint test
    translated_to_fr = translator.english_to_french(textToTranslate)
    return translated_to_fr

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    #i have renamed the method after pylint test
    translated_to_en = translator.french_to_english(textToTranslate)
    return translated_to_en

@app.route("/")
def renderIndexPage():
    # Write the code to render template

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
