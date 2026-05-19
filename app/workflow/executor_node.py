from tools.tool_registry import TOOLS

from tools.tool_router import select_tools


def executor_node(state):

    query = state["query"]

    intent = state["intent"]

    observations = []

    print("\nEXECUTION ENGINE:\n")

    # Select tools
    selected_tools = select_tools(
        query,
        intent
    )

    print(f"Selected Tools: {selected_tools}")

    # Temporary ticker
    ticker = "AAPL"

    # Execute tools safely
    for tool_name in selected_tools:

        try:

            tool_function = TOOLS[tool_name]["function"]

            # Intent-aware execution
            if tool_name == "company_news":

                output = tool_function(
                    ticker,
                    intent
                )

            else:

                output = tool_function(ticker)

            observations.append({

                "tool": tool_name,

                "output": output,

                "status": "success"
            })

            print(f"\n--- {tool_name} OUTPUT ---\n")

            print(output)

        except Exception as e:

            error_message = str(e)

            observations.append({

                "tool": tool_name,

                "output": error_message,

                "status": "failed"
            })

            print(f"\n--- {tool_name} FAILED ---\n")

            print(error_message)

    # Save observations
    state["observations"] = observations

    return state