from tools.financial_api import (

    get_stock_price,

    get_company_info,

    get_company_news
)

from tools.sec_tool import get_sec_filings


TOOLS = {

    "stock_price": {

        "function": get_stock_price,

        "description":
        "Get current stock price for a company ticker"
    },

    "company_info": {

        "function": get_company_info,

        "description":
        "Get company profile and business information"
    },

    "company_news": {

        "function": get_company_news,

        "description":
        "Get latest company news headlines"
    },

    "sec_filings": {

        "function": get_sec_filings,

        "description":
        "Retrieve SEC filing risk disclosures and regulatory evidence"
    }
}