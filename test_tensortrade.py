import tensortrade.env.default as default
from tensortrade.data.cdd import CryptoDataDownload

# Baixar dados históricos de Bitcoin/USD
cdd = CryptoDataDownload()
data = cdd.fetch("Binance", "USD", "BTC/USD", "1h")

# Criar o ambiente de trading
environment = default.create(
    data=data,
    window_size=20,
    hold_threshold=0.5,
    max_allowed_slippage_percent=1,
    trade_instrument='BTC',
    fiat_instrument='USD',
    base_precision=5,
    instrument_precision=6,
)

# Exibir as primeiras linhas dos dados
print(data.head())
print("\nEnvironment created successfully.")
