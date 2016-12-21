from flask import Flask, render_template, request
import  nltk
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result.html', methods=['POST'])
def tokenizer():
    text = request.form['text']
    pisht = str(text)
    result = str.split(pisht)
    string=str(result)
    return string

if __name__ == '__main__':
    app.run(debug = "True")
