from flask import Flask, request, render_template
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/translate', methods=['GET','POST'])
def translate():
    if request.method == 'POST':
        text = request.form['text_to_translate']
        language_selected = request.form['select-language']
        result = translator.translate(text, dest=language_selected)
        text = result.text
    return render_template('index.html', translation_result=text)
    


if __name__ == "__main__":
    app.run(debug=True)

