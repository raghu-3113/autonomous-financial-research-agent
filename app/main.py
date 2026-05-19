from workflow.graph_builder import build_graph

graph = build_graph()

initial_state = {

    "intent": "",

    "query": "What is Apple's stock price?",

    "plan": "",

    "observations": [],

    "retrieved_docs": [],

    "final_response": ""

    ,"verification_report": ""
}

result = graph.invoke(initial_state)

print("\nWORKFLOW COMPLETED")