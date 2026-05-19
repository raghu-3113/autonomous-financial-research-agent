def prioritize_observations(
    observations,
    intent
):

    priority_map = {

        "risk_analysis": [
            "sec_filings",
            "company_info",
            "company_news"
        ],

        "company_overview": [
            "company_info",
            "sec_filings",
            "company_news"
        ],

        "stock_analysis": [
            "stock_price",
            "company_info"
        ],

        "news_research": [
            "company_news",
            "company_info"
        ]
    }

    priorities = priority_map.get(
        intent,
        []
    )

    sorted_observations = sorted(

        observations,

        key=lambda obs:

        priorities.index(obs["tool"])

        if obs["tool"] in priorities

        else 999
    )

    return sorted_observations