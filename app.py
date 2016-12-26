 #!/usr/bin/python
 # -*- coding: utf-8 -*-
from __future__ import unicode_literals
from flask import Flask, render_template, request
import nltk
from hazm import *
import os
import codecs
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ResultToken.html', methods=['GET'])
def tokenizer():
    text = request.args[u'TokenText']
    result = word_tokenize(text)
    string = str(result)
    return string


@app.route('/ResultNorm.html', methods=['GET'])
def normalize():
    NormText = request.args[u'NormText']
    normalizer = Normalizer()
    ResultNorm = normalizer.normalize(NormText)
    StringNorm = str(ResultNorm)
    return StringNorm

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

