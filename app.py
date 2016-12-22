 #!/usr/bin/python
 # -*- coding: utf-8 -*-
from __future__ import unicode_literals
from flask import Flask, render_template, request
import nltk
from hazm import *
import os
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result.html', methods=['POST'])
def tokenizer():
    text = request.form['text']
    pisht = str(text)
    encode = unicode(pisht, "utf-8")
    result = sent_tokenize(encode)
    string = str(result)
    print = print(string)
    return print

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

