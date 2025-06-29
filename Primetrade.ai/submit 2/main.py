from binance.um_futures import UMFutures

# Replace with your actual API key and secret
api_key = 'dbefbc809e3e83c283a984c3a1459732ea7db1360ca80c5c2c8867408d28cc83'
api_secret = '2b5eb11e18796d12d88f13dc27dbbd02c2cc51ff7059765ed9821957d82bb4d9'

# Initialize the client
client = UMFutures(key=api_key, secret=api_secret)

try:
    # Place a LIMIT BUY order
    response = client.new_order(
        symbol="BTCUSDT",
        side="BUY",
        type="LIMIT",
        timeInForce="GTC",
        price="42088.0",
        quantity="0.1"
    )
    print("Order Response:", response)
except Exception as e:
    print("Error placing order:", e)
