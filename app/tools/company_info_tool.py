import yfinance as yf

def get_company_info(ticker):

    stock = yf.Ticker(ticker)

    info = stock.info

    company_data = {
        "Company": info.get("longName"),
        "Sector": info.get("sector"),
        "Market Cap": info.get("marketCap"),
        "Website": info.get("website")
    }

    return company_data