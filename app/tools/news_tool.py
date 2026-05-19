import yfinance as yf


def get_company_news(
    ticker,
    intent="general"
):

    stock = yf.Ticker(ticker)

    news = stock.news

    filtered_news = []

    # Risk-focused filtering
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

        # Risk-analysis mode
        if intent == "risk_analysis":

            if any(

                keyword.lower() in title.lower()

                for keyword in risk_keywords
            ):

                filtered_news.append(title)

        else:

            filtered_news.append(title)

    return filtered_news[:5]