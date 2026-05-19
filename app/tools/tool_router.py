from utils.llm import ask_llm

from tools.tool_registry import TOOLS


def select_tools(query, intent):

    # Build tool descriptions
    tool_descriptions = ""

    for tool_name, tool_data in TOOLS.items():

        tool_descriptions += f"""
Tool Name: {tool_name}
Description: {tool_data['description']}
"""

    # Intent-aware routing prompt
    prompt = f"""
You are an autonomous financial tool router.

Detected Query Intent:
{intent}

Available Tools:
{tool_descriptions}

User Query:
{query}

Your task:
Select ONLY the MOST relevant tools.

Guidelines:

- company_overview:
  Prefer company_info

- stock_analysis:
  Prefer stock_price + company_info

- news_research:
  Prefer company_news

- risk_analysis:
  Prefer sec_filings + company_news

- sec_filing_analysis:
  Prefer sec_filings

- financial_performance:
  Prefer company_info + sec_filings

Return ONLY comma-separated tool names.

Example:
stock_price, company_info
"""

    response = ask_llm(prompt)

    print("\nTOOL ROUTER OUTPUT:\n")

    print(response)

    # Parse LLM-selected tools
    selected_tools = [

        tool.strip()

        for tool in response.split(",")

        if tool.strip() in TOOLS
    ]

    # HARD TOOL POLICIES

    if intent == "risk_analysis":

        # SEC filings REQUIRED
        if "sec_filings" not in selected_tools:

            selected_tools.insert(
                0,
                "sec_filings"
            )

        # Supporting company info
        if "company_info" not in selected_tools:

            selected_tools.append(
                "company_info"
            )

    # Company overview constraints
    elif intent == "company_overview":

        selected_tools = [

            tool

            for tool in selected_tools

            if tool != "company_news"
        ]

        if "company_info" not in selected_tools:

            selected_tools.insert(
                0,
                "company_info"
            )

    # Stock analysis constraints
    elif intent == "stock_analysis":

        required = [
            "stock_price",
            "company_info"
        ]

        for tool in required:

            if tool not in selected_tools:

                selected_tools.append(tool)

    # Fallback
    if not selected_tools:

        selected_tools = ["company_info"]

    return selected_tools