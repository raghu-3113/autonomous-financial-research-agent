from utils.llm import ask_llm

from filters.relevance_filter import filter_observations

from filters.source_prioritizer import prioritize_observations


def synthesis_node(state):

    query = state["query"]

    observations = state["observations"]

    # Keep only successful tools
    observations = [

        obs

        for obs in observations

        if obs.get("status") == "success"
    ]

    # Filter irrelevant observations
    observations = filter_observations(
        query,
        observations
    )

    # Prioritize evidence
    intent = state["intent"]

    observations = prioritize_observations(
        observations,
        intent
    )

    # Combine observations
    combined_observations = ""

    for obs in observations:

        combined_observations += f"""
Tool:
{obs['tool']}

Output:
{obs['output']}

"""

    # Grounded synthesis prompt
    prompt = f"""
You are a professional financial research analyst.

Your task:
Generate a STRICTLY evidence-grounded analysis.

User Query:
{query}

Retrieved Evidence:
{combined_observations}

IMPORTANT RULES:

1. ONLY use facts explicitly supported
by the retrieved evidence.

2. DO NOT speculate.

3. DO NOT infer hidden motives,
future outcomes, or political implications
unless directly supported.

4. If evidence is weak or incomplete,
explicitly state the limitation.

5. Prefer conservative financial analysis.

6. Avoid dramatic language.

Return structured output:

1. Key findings
2. Identified risks/opportunities
3. Evidence limitations
"""

    # Generate synthesis
    final_response = ask_llm(prompt)

    print("\nFINAL SYNTHESIS:\n")

    print(final_response)

    # Save response
    state["final_response"] = final_response

    # Store retrieved docs
    state["retrieved_docs"] = [

        str(obs["output"])

        for obs in observations
    ]

    return state