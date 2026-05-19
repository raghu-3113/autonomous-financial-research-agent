from typing import TypedDict, List, Dict

class AgentState(TypedDict):

    query: str

    intent: str

    plan: str

    observations: List[Dict]

    retrieved_docs: List[str]

    final_response: str

    verification_report: str