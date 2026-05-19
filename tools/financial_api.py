import yfinance as yf

def get_stock_price(ticker):

    stock = yf.Ticker(ticker)

    data = stock.history(period="1d")

    return round(data["Close"].iloc[-1], 2)


def get_company_info(ticker):

    stock = yf.Ticker(ticker)

    info = stock.info

    return {
        "Company": info.get("longName"),
        "Sector": info.get("sector"),
        "Market Cap": info.get("marketCap"),
        "Website": info.get("website")
    }


def get_company_news(ticker):

    stock = yf.Ticker(ticker)

    news = stock.news[:5]

    headlines = []

    for item in news:

        headlines.append(item.get("title"))

    return headlines