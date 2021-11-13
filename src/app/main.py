# -*- coding: utf-8 -*-
import pickle
import numpy as np
import os
from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth
from sklearn.preprocessing import StandardScaler
import pandas as pd

colunas = ['ligacao_consumidor',
            'nota_consumidor',
            'custo_do_produto',
            'compras_anteriores',
            'desconto_oferecido',
            'peso_em_gms',
            'bloco_deposito_A',
            'bloco_deposito_B',
            'bloco_deposito_C',
            'bloco_deposito_D',
            'bloco_deposito_F',
            'forma_envio_Flight',
            'forma_envio_Road',
            'forma_envio_Ship',
            'genero_consumidor_F',
            'genero_consumidor_M',
            'importancia_produto_high',
            'importancia_produto_low',
            'importancia_produto_medium'
        ]

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = os.environ.get('BASIC_AUTH_USERNAME')
app.config['BASIC_AUTH_PASSWORD'] = os.environ.get('BASIC_AUTH_PASSWORD')

basic_auth = BasicAuth(app)

def load_model(file_name):
    return pickle.load(open(file_name, "rb"))

modelo = load_model('models/modelo_gnb.pkl')

# Rota para utilização de modelo treinado para predição
@app.route('/predict/', methods=['POST'])
@basic_auth.required
def predict():    
    dados = request.get_json()
    # payload = [dados[col] for col in colunas]
    sc = StandardScaler()
    df_train = pd.read_csv('src/data/X_train.csv')
    df_payload = pd.DataFrame({key: [dados[key]] for key in dados})
    sc.fit_transform(df_train)
    X_test = sc.transform(df_payload)
    score = np.float64(modelo.predict_proba(X_test)[:,1])
    
    status = 'Alerta! Produto com altas chances de atraso.'
    if score <= 0.4:
        status = 'Chance baixa de atraso.'
    elif score <= 0.6: 
        status = 'Chance média de atraso, verifique.'

    return jsonify(status=status)

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
