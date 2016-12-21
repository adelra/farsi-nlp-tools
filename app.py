from flask import Flask, render_template, request
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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
