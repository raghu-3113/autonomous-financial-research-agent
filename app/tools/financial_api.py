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


def get_company_news(
    ticker,
    intent="general"
):

    stock = yf.Ticker(ticker)

    news = stock.news

    filtered_news = []

    risk_keywords = [

        "risk",

        "lawsuit",

        "regulation",

        "supply chain",

        "cybersecurity",

        "investigation",

        "decline",

        "warning",

        "antitrust",

        "competition"
    ]

    for article in news[:15]:

        title = article.get("title", "")

        if intent == "risk_analysis":

            if any(

                keyword.lower() in title.lower()

                for keyword in risk_keywords
            ):

                filtered_news.append(title)

        else:

            filtered_news.append(title)

    return filtered_news[:5]
