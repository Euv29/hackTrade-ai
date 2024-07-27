# app.py
from flask import Flask, render_template, jsonify
import pandas as pd
import ccxt
import json
from binance_data import fetch_binance_data
from trading_env import create_env
from stable_baselines3 import PPO

app = Flask(__name__)

# Carregar o modelo treinado
model = PPO.load("models/trading_model")

@app.route('/data')
def get_data():
    df = fetch_binance_data('BTC/USDT', '1h')
    return jsonify(df.reset_index().to_dict(orient='records'))

@app.route('/signals')
def get_signals():
    env = create_env()
    obs = env.reset()
    action, _states = model.predict(obs, deterministic=True)
    return jsonify({
        'action': int(action[0]),
        'info': 'Buy' if action[0] == 1 else 'Sell'  # Exemplo, ajuste conforme a lógica
    })

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
