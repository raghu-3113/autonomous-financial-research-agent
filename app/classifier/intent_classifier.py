from utils.llm import ask_llm

def classify_query(query):

    prompt = f"""
You are a financial query classifier.

Classify the user's query into ONE category only.

Categories:

1. company_overview
2. stock_analysis
3. news_research
4. risk_analysis
5. sec_filing_analysis
6. financial_performance

User Query:
{query}

Return ONLY the category name.
"""

    response = ask_llm(prompt)

    return response.strip().lower()