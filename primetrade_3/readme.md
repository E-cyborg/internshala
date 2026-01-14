# Binance Futures Testnet Bot

A simple Python bot that places **MARKET** and **LIMIT** orders on Binance Futures Testnet.

## Setup

    # Create virtual environment
    python -m venv .venv

    # Activate it (Windows)
    .venv\Scripts\activate

    # Install dependencies
    pip install -r requirements.txt

## Usage

### Place a Market Buy Order

    python basicbot.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.001

### Place a Limit Sell Order

    python basicbot.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.001 --price 30000

## Notes
- Uses Binance **Futures Testnet** API only.
- Requires your **API Key** and **Secret Key** from Binance Testnet.
- Edit `basicbot.py` or set keys via environment variables before running.
