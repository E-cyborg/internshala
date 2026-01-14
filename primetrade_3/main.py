
import time, hmac, hashlib, json, requests, argparse, logging
from urllib.parse import urlencode

BASE_URL = "https://testnet.binancefuture.com" 
API_KEY ='dbefbc809e3e83c283a984c3a1459732ea7db1360ca80c5c2c8867408d28cc83'
SECRET_KEY='2b5eb11e18796d12d88f13dc27dbbd02c2cc51ff7059765ed9821957d82bb4d9'







logging.basicConfig(
    filename="basicbot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class BasicBot:
    def __init__(self, api_key, api_secret, base_url=BASE_URL):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = base_url
        self.headers = {"X-MBX-APIKEY": self.api_key}

    def _get_server_time(self):
        url = f"{self.base_url}/fapi/v1/time"
        return requests.get(url, timeout=10).json()["serverTime"]

    def _sign(self, params):
        params["timestamp"] = self._get_server_time()
        query = urlencode(params)
        sig = hmac.new(self.api_secret.encode(), query.encode(), hashlib.sha256).hexdigest()
        params["signature"] = sig
        return params

    def place_order(self, symbol, side, order_type, qty, price=None):
        url = f"{self.base_url}/fapi/v1/order"
        params = {"symbol": symbol, "side": side, "type": order_type, "quantity": qty}
        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        signed = self._sign(params)
        r = requests.post(url, headers=self.headers, params=signed)
        try:
            r.raise_for_status()
            data = r.json()
            logging.info(f"Order success: {data}")
            return data
        except Exception as e:
            logging.error(f"Order failed: {r.text}")
            return {"error": str(e), "details": r.text}



# --- CLI ---
def main():
    parser = argparse.ArgumentParser(description="Basic Binance Futures Bot")
    parser.add_argument("--symbol", required=True, help="e.g. BTCUSDT")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--qty", required=True, type=float, help="Quantity")
    parser.add_argument("--price", type=float, help="Price (for LIMIT orders)")
    args = parser.parse_args()

    bot = BasicBot(API_KEY, SECRET_KEY)
    result = bot.place_order(args.symbol, args.side, args.type, args.qty, args.price)
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
