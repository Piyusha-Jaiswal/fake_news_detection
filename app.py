from flask import Flask, jsonify, request, render_template
from PredictionModel import PredictionModel
import pandas as pd
from random import randrange

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():
    text = request.json['text']
    model = PredictionModel(text)
    return jsonify(model.predict())


@app.route('/random', methods=['GET'])
def random():
    data = pd.read_csv("jupiter_code/fake-news/test.csv")
    index = randrange(0, len(data)-1, 1)
    return jsonify({'title': data.loc[index].title, 'author': data.loc[index].author, 'text': data.loc[index].text})



# Only for local running
if __name__ == '__main__':
    app.run()
