import yfinance as yf
from nsepython import nse_eq
from pprint import pprint

def fetch_stock_data(symbol):
    """Fetch stock data using NSE and Yahoo Finance for detailed insights."""
    try:
        # ✅ Fetch data from NSE
        stock_data = nse_eq(symbol.upper())
        price_info = stock_data.get("priceInfo", {})
        metadata = stock_data.get("metadata", {})

        last_price = price_info.get("lastPrice", 0)
        prev_close = price_info.get("previousClose", 0)
        open_price = price_info.get("open", 0)
        vwap = price_info.get("vwap", 0)

        high_price = price_info.get("intraDayHighLow", {}).get("max", 0)
        low_price = price_info.get("intraDayHighLow", {}).get("min", 0)

        week_high = price_info.get("weekHighLow", {}).get("max", 0)
        week_low = price_info.get("weekHighLow", {}).get("min", 0)

        change = price_info.get("change", 0)
        p_change = price_info.get("pChange", 0)

        # ✅ Fetch additional data from Yahoo Finance
        yahoo_symbol = f"{symbol}.NS"  # Yahoo Finance uses '.NS' for NSE stocks
        stock = yf.Ticker(yahoo_symbol)
        yahoo_info = stock.info

        pe_ratio = yahoo_info.get("trailingPE", "N/A")
        pb_ratio = yahoo_info.get("priceToBook", "N/A")
        market_cap = yahoo_info.get("marketCap", "N/A")
        dividend_yield = yahoo_info.get("dividendYield", "N/A")
        sector = metadata["industry"]

        # Determine trend
        trend = "📈 Uptrend" if last_price > prev_close else "📉 Downtrend"

        # Check breakout & reversal zones
        near_week_high = last_price >= week_high * 0.98 if week_high else False
        near_week_low = last_price <= week_low * 1.02 if week_low else False

        breakout_status = "🚀 Near 52-week high. Possible breakout!" if near_week_high else ""
        reversal_status = "🔻 Near 52-week low. Possible reversal." if near_week_low else ""

        # Determine VWAP position
        vwap_status = "✅ Above VWAP (Bullish)" if last_price > vwap else "❌ Below VWAP (Bearish)"

        # Print insights
        print(f"\n📊 Stock Analysis for {symbol.upper()} ({metadata.get('companyName', 'N/A')})")
        print(f"🔹 Last Price: ₹{last_price}")
        print(f"🔄 Change: ₹{change} ({p_change}%)")
        print(f"📈 Open Price: ₹{open_price}")
        print(f"📊 Day Low: ₹{low_price} | 📊 Day High: ₹{high_price}")
        print(f"📌 52-Week Low: ₹{week_low} | 📌 52-Week High: ₹{week_high}")
        print(f"📍 VWAP: ₹{vwap} | {vwap_status}")
        print(f"📊 Trend: {trend}")
        print(f"Primary Index: {metadata['pdSectorInd']}")
        print("Other Indexes\n")
        for i in metadata["pdSectorIndAll"]:
            print(f" {i}")
        pesector=metadata["pdSectorPe"]
        pesymbol=metadata["pdSymbolPe"]
        if pesector>pesymbol:
            print("Stock is UnderPriced")
        elif pesymbol>pesector:
            print("Stock is OverPriced")
        else:
            print("Stock Is Fairly Priced")
        listingDate=metadata["listingDate"]
        print(f"Listing Date: {listingDate}")
        isin = metadata["isin"]
        print(f"ISIN Number: {isin}")
        # Yahoo Finance Data
        print("\n💹 Additional Yahoo Finance Data:")
        print(f"🏢 Sector: {sector}")
        print(f"💰 Market Cap: ₹{market_cap}")
        print(f"📊 PE Ratio: {pe_ratio} | 📖 PB Ratio: {pb_ratio}")
        print(f"💸 Dividend Yield: {dividend_yield}")

        if breakout_status:
            print(f"🚀 {breakout_status}")
        if reversal_status:
            print(f"📉 {reversal_status}")

    except Exception as e:
        print("\n❌ Error fetching stock data. Check the stock symbol.")
        print(f"Error: {e}")

# Example usage
fetch_stock_data("BHARTIARTL")  # Replace with any NSE stock symbol
