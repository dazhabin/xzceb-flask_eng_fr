"""
Flask app for translating english to french and french to english
"""
from flask import Flask, render_template, request
from machinetranslation import translator
#import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french():
    """
    Returns text translated from english to french.
    """
    text_to_translate = request.args.get('textToTranslate')
    # Write your code here
    return translator.english_to_french(text_to_translate)

@app.route("/frenchToEnglish")
def french_to_english():
    """
    Returns text translated from french to english.
    """
    text_to_translate = request.args.get('textToTranslate')
    # Write your code here
    return translator.french_to_english(text_to_translate)
#    return "Translated text to English"

@app.route("/")
def render_index_page():
    """
    Renders index.html template as root page
    """
    # Write the code to render template
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
