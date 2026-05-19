from tools.sec_tool import get_sec_filings
from tools.financial_api import (
    get_stock_price,
    get_company_info,
    get_company_news
)

TOOLS = {
    "sec_filings": {

    "function": get_sec_filings,

    "description": "Retrieve latest SEC filings including 10-K reports",

    "keywords": [
        "sec",
        "filing",
        "10-k",
        "annual report",
        "regulatory filing",
        "financial filing"
    ]
},

    "stock_price": {

        "function": get_stock_price,

        "description": "Get current stock price for a company ticker",

        "keywords": [
            "stock",
            "price",
            "market price",
            "share price"
        ]
    },

    "company_info": {

        "function": get_company_info,

        "description": "Get company profile and business information",

        "keywords": [
    "company",
    "profile",
    "sector",
    "business",
    "market cap",
    "information",
    "details"
]
        
    },

    "company_news": {

        "function": get_company_news,

        "description": "Get latest company news headlines",

        "keywords": [
    "news",
    "latest",
    "headlines",
    "updates",
    "recent",
    "announcement",
    "developments",
    "media"
]
        ]
    }
}