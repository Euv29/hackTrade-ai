# binance_client.py

import ccxt
import config

class BinanceClient:
    def __init__(self):
        self.exchange = ccxt.binance({
            'apiKey': config.BINANCE_API_KEY,
            'secret': config.BINANCE_API_SECRET,
        })

    def get_ohlcv(self, symbol, timeframe='1d', since=None, limit=100):
        return self.exchange.fetch_ohlcv(symbol, timeframe, since, limit)
