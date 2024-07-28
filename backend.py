from flask import Flask, jsonify, render_template
from binance.client import Client
import config

app = Flask(__name__)

client = Client(config.BINANCE_API_KEY, config.BINANCE_API_SECRET)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ohlcv/<symbol>/<interval>', methods=['GET'])
def ohlcv(symbol, interval):
    klines = client.get_klines(symbol=symbol, interval=interval)
    return jsonify(klines)

@app.route('/ohlcv/<symbol>/<interval>', methods=['GET'])
def ohlcv(symbol, interval):
    try:
        ohlcv_data = get_binance_ohlcv(symbol, interval)
        print(ohlcv_data)  
        return jsonify(ohlcv_data)
    except Exception as e:
        print(f"Error: {e}")  
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
