import json

import os

from datetime import datetime


MEMORY_FILE = os.path.abspath(

    os.path.join(

        os.path.dirname(__file__),

        "../../outputs/memory/research_memory.json"
    )
)


def save_memory(state):

    memory_entry = {

        "timestamp":
        str(datetime.now()),

        "query":
        state["query"],

        "intent":
        state["intent"],

        "final_response":
        state["final_response"]
    }

    # Load existing memory
    if os.path.exists(MEMORY_FILE):

        with open(
            MEMORY_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            try:

                memory = json.load(f)

            except:

                memory = []

    else:

        memory = []

    # Append new entry
    memory.append(memory_entry)

    # Save updated memory
    with open(
        MEMORY_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            memory,
            f,
            indent=4
        )


def build_context():

    if not os.path.exists(MEMORY_FILE):

        return "No previous memory."

    with open(
        MEMORY_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        try:

            memory = json.load(f)

        except:

            return "No previous memory."

    if not memory:

        return "No previous memory."

    # Last 3 sessions
    recent_memory = memory[-3:]

    context = ""

    for item in recent_memory:

        context += f"""

Previous Query:
{item['query']}

Intent:
{item['intent']}

Summary:
{item['final_response'][:500]}

"""

    return context