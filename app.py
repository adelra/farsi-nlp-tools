from flask import Flask, render_template, request
import nltk
#from nltk.tokenize import StanfordTokenizer
app = Flask(__name__)
import os

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result.html', methods=['POST'])
def tokenizer():
    text = request.form['text']
    pisht = str(text)
    result = StanfordTokenizer().tokenize(pisht)
    string=str(result)
    return string

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
