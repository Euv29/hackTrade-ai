# binance_data.py
import ccxt
import pandas as pd

def fetch_binance_data(symbol, timeframe, limit=1000):
    binance = ccxt.binance()
    ohlcv = binance.fetch_ohlcv(symbol, timeframe, limit=limit)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)
    return df

if __name__ == "__main__":
    df = fetch_binance_data('BTC/USDT', '1h')
    print(df.head())
