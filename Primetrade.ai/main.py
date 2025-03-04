import pandas as pd
import requests
import time
import xlwings as xw
import os

# File path for the Excel sheet
file_path = r"" # plese enter your path 

# Fetch live cryptocurrency data
def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 50,
        "page": 1,
        "sparkline": "false"
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"⚠️ API request failed: {e}")
        return None

# Analyze data: Find top 5 cryptos, average price, highest & lowest 24h change
def analyze_crypto_data(data):
    df = pd.DataFrame(data, columns=['name', 'current_price', 'market_cap', 'total_volume', 
                                     'price_change_percentage_24h', 'market_cap_rank'])

    top_5 = df.nlargest(5, 'market_cap')[['name', 'market_cap']]
    avg_price = df['current_price'].mean()
    highest_change = df.nlargest(1, 'price_change_percentage_24h')[['name', 'price_change_percentage_24h']]
    lowest_change = df.nsmallest(1, 'price_change_percentage_24h')[['name', 'price_change_percentage_24h']]

    return df, top_5, avg_price, highest_change, lowest_change



# Update Excel with live data
def update_excel():
    try:
        # Check if file exists, otherwise create it
        if not os.path.exists(file_path):
            wb = xw.Book()
            wb.save(file_path)
            wb.close()
        
        
        wb = xw.Book(file_path)
        ws = wb.sheets[0]

        new_data = fetch_crypto_data()
        if new_data:
            df, top_5, avg_price, highest_change, lowest_change = analyze_crypto_data(new_data)

            # Update main data
            ws.range("A1").value = ["Name", "Current Price", "Market Cap", "Total Volume",
                                    "24h Price Change (%)", "Market Cap Rank"]
            ws.range("A2").value = df.values  # Main data
            
            # Update analysis
            ws.range("H1").value = "Analysis"
            ws.range("H2").value = ["Top 5 by Market Cap"]
            ws.range("H3").value = top_5.values
            ws.range("H9").value = f"Average Price: {avg_price:.2f} USD"
            ws.range("H10").value = f"Highest 24h Change: {highest_change.iloc[0,0]} ({highest_change.iloc[0,1]:.2f}%)"
            ws.range("H11").value = f"Lowest 24h Change: {lowest_change.iloc[0,0]} ({lowest_change.iloc[0,1]:.2f}%)"

            print("✅ Excel updated successfully!")

        else:
            print("❌ No new data available.")

    except Exception as e:
        print(f"⚠️ Error updating Excel: {e}")

# Run update every 5 minutes
while True:
    update_excel()
    print("Waiting 5 minutes for next update...")
    time.sleep(60 * 5)
