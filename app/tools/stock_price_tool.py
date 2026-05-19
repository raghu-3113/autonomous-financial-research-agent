import yfinance as yf

def get_stock_price(ticker):

    stock = yf.Ticker(ticker)

    data = stock.history(period="1d")

    latest_price = data["Close"].iloc[-1]

    return f"Current stock price of {ticker} is ${latest_price:.2f}"