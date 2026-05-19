from utils.llm import ask_llm

from memory.context_manager import build_context

from classifier.intent_classifier import classify_query


def planner_node(state):

    query = state["query"]

    # Detect intent
    intent = classify_query(query)

    state["intent"] = intent

    print("\nDETECTED INTENT:\n")

    print(intent)

    # Memory context
    memory_context = build_context()

    # Planner prompt
    prompt = f"""
You are an autonomous financial research planner.

Detected Query Intent:
{intent}

Your task:
Create a focused research plan ONLY relevant
to this intent category.

Previous Memory Context:
{memory_context}

Current Query:
{query}

Return:
- research objectives
- required information
- likely financial tools needed
"""

    # Generate plan
    plan = ask_llm(prompt)

    print("\nPLANNER OUTPUT:\n")

    print(plan)

    # Save plan
    state["plan"] = plan

    return state