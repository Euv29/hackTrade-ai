# trading_env.py
import tensortrade as tt
from tensortrade.oms.exchanges import Exchange
from tensortrade.oms.instruments import USD, BTC
from tensortrade.oms.services.execution.simulated import execute_order
from tensortrade.feed.core import DataFeed, Stream
import pandas as pd
from binance_data import fetch_binance_data
from stable_baselines3 import PPO

def create_env():
    df = fetch_binance_data('BTC/USDT', '1h')
    price = Stream.source(df['close'].tolist(), dtype="float").rename("BTC-USDT")
    feed = DataFeed([price])
    
    exchange = Exchange("simulated", service=execute_order)(
        Stream.source(df['close'].tolist(), dtype="float").rename("BTC-USDT")
    )
    
    env = tt.environments.default.create(
        feed=feed,
        portfolio=tt.Portfolio(USD, [
            tt.Wallet(exchange, 1000 * USD),
            tt.Wallet(exchange, 1 * BTC)
        ]),
        action_scheme="managed-risk",
        reward_scheme="simple",
        window_size=10
    )
    
    return env

def train_model():
    env = create_env()
    model = PPO("MlpPolicy", env, verbose=1)
    model.learn(total_timesteps=10000)
    model.save("trading_model")
    
if __name__ == "__main__":
    train_model()
