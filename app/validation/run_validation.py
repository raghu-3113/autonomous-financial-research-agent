from workflow.graph_builder import build_graph

from validation.challenge_suite import CHALLENGES


graph = build_graph()

print("\nRUNNING VALIDATION SUITE\n")


for challenge in CHALLENGES:

    print("\n====================")

    print(f"Challenge {challenge['id']}")

    print("====================\n")

    print(f"Query: {challenge['query']}")

    initial_state = {

        "query":
        challenge["query"],

        "intent": "",

        "plan": "",

        "observations": [],

        "retrieved_docs": [],

        "final_response": "",

        "verification_report": ""
    }

    result = graph.invoke(
        initial_state
    )

    print("\nCOMPLETED\n")