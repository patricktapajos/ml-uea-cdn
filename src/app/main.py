# -*- coding: utf-8 -*-
import pickle
from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth
import os

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = os.environ.get('BASIC_AUTH_USERNAME')
app.config['BASIC_AUTH_PASSWORD'] = os.environ.get('BASIC_AUTH_PASSWORD')

basic_auth = BasicAuth(app)

# def load_model(file_name):
#     return pickle.load(open(file_name, "rb"))

# modelo = load_model('models/xgboost_undersampling.pkl')

# Rota para utilização de modelo treinado para predição
@app.route('/predict/', methods=['POST'])
@basic_auth.required
def predict():    
    return jsonify(status='OK')

# Rota para teste de endpoint
@app.route('/test/<param>')
@basic_auth.required
def test(param):
    return 'Teste de endpoint com parâmetro: {}'.format(param)

# Rota padrão
@app.route('/')
def home():
    return 'API de algum projeto legal :)'

# Subir a API
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
