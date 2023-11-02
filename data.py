import os
import datetime as dt
import pandas as pd
import requests
from dotenv import load_dotenv
import mplfinance as mpf
load_dotenv()


class AlpacaDataClient:
    def __init__(self):
        self.alpaca_data_secret = os.environ.get('ALPACA_DATA_SECRET_KEY')
        self.alpaca_data_public = os.environ.get('ALPACA_DATA_PUBLIC_KEY')
        if self.alpaca_data_secret is None or self.alpaca_data_public is None:
            raise Exception("Alpaca keys not found in environment variables!")
        self.alpaca_data_url = 'https://data.alpaca.markets/v2/'
        self.headers = {"accept": "application/json", 'APCA-API-KEY-ID': self.alpaca_data_public, 'APCA-API-SECRET-KEY': self.alpaca_data_secret}
        self.start_data = dt.datetime.now() - dt.timedelta(days=365)
        self.end_data = dt.datetime.now()
        # Format as YYY-MM-DD
        self.start_data = self.start_data.strftime('%Y-%m-%d')
        self.end_data = self.end_data.strftime('%Y-%m-%d')

    def do_get(self, url, params):
        result = requests.get(url, headers=self.headers, params=params)
        return result
    
    def get_bars(self, symbols, timeframe="1D", start=None, end=None, adjustment="raw", limit=1000, asof=None, feed="iex", currency="USD", page_token=None, only_market=False):
        # API Link: https://docs.alpaca.markets/reference/stockbars
        if start is None:
            start = self.start_data
        if end is None:
            end = self.end_data
        if asof is None:
            asof = dt.datetime.now().strftime('%Y-%m-%d')
        url = self.alpaca_data_url + 'stocks/bars'
        params = {
                    'symbols': symbols,
                    'timeframe': timeframe,
                    'start': start,
                    'end': end,
                    'adjustment': adjustment,
                    'limit': limit,
                    'asof': asof,
                    'feed': feed,
                    'currency': currency,
                    'page_token': page_token
                    }
        result = self.do_get(url, params)
        try:
            data = result.json()
        except:
            print("Error retrieving bars: " + result.text)
            return None
        if (len(symbols.split(",")) > 1):
            dfs = {}
            for symbol in symbols.split(","):
                dfs[symbol] = pd.DataFrame(data["bars"][symbol])
                dfs[symbol].set_index("t", inplace=True)
                dfs[symbol].index = pd.to_datetime(df.index, format='%Y-%m-%dT%H:%M:%S.%fZ')
                dfs[symbol].index.name = "time"
                # Make column names more specific
                dfs[symbol].rename(columns={"o": "open", "h": "high", "l": "low", "c": "close", "v": "volume", "n": "trades", "vw": "volume weighted"}, inplace=True)
                if only_market:
                    # Restrict time to market hours, our data is in UTC
                    dfs[symbol] = dfs[symbol].between_time('13:30', '20:00')
            return dfs
        df = pd.DataFrame(data["bars"][symbols])
        df.set_index("t", inplace=True)
        df.index.name = "time"
        df.index = pd.to_datetime(df.index, format='%Y-%m-%dT%H:%M:%S%fZ')
        # Make column names more specific
        df.rename(columns={"o": "open", "h": "high", "l": "low", "c": "close", "v": "volume", "n": "trades", "vw": "volume weighted"}, inplace=True)
        if (only_market):
            # Restrict time to market hours
            df = df.between_time('13:30', '20:00')
        return df
    

    def plot_candlestick(self, symbol, timeframe="1D", start=None, end=None):
            df = self.get_bars(symbol, timeframe=timeframe, start=start, end=end)
            if df is not None:
                mpf.plot(df, type='candle', style='charles',
                        title=symbol,
                        ylabel='Price ($)',
                        ylabel_lower='Volume',
                        volume=True)
# Usage
# Create an instance of your class, then call the plot_candlestick function
obj = AlpacaDataClient()
obj.plot_candlestick("AAPL", start="2023-01-01", end="2023-01-31")