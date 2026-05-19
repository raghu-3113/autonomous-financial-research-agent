from langgraph.graph import StateGraph, END

from workflow.state import AgentState

from workflow.planner import planner_node
from workflow.executor_node import executor_node
from workflow.synthesis_node import synthesis_node
from workflow.verification_node import verification_node

def build_graph():

    workflow = StateGraph(AgentState)

    # Nodes
    workflow.add_node("planner", planner_node)

    workflow.add_node("executor", executor_node)

    workflow.add_node("synthesis", synthesis_node)

    workflow.add_node("verification", verification_node)

    # Entry
    workflow.set_entry_point("planner")

    # Flow
    workflow.add_edge("planner", "executor")

    workflow.add_edge("executor", "synthesis")

    workflow.add_edge("synthesis", "verification")

    workflow.add_edge("verification", END)

    return workflow.compile()