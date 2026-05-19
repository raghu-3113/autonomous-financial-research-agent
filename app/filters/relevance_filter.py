from utils.llm import ask_llm

def filter_observations(
    query,
    observations
):

    filtered = []

    for obs in observations:

        prompt = f"""
You are a financial relevance evaluator.

User Query:
{query}

Observation:
{obs['output']}

Task:
Determine whether this observation is
HIGHLY relevant to answering the query.

Return ONLY:
relevant
or
irrelevant
"""

        response = ask_llm(prompt)

        decision = response.strip().lower()

        if "relevant" in decision:

            filtered.append(obs)

    return filtered