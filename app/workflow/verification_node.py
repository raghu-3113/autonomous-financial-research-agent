from utils.llm import ask_llm

from memory.context_manager import save_memory
from reports.report_generator import generate_report

from evaluation.evaluator import evaluate_workflow


def verification_node(state):

    query = state["query"]

    retrieved_docs = state["retrieved_docs"]

    final_response = state["final_response"]

    # Combine evidence
    evidence = "\n\n".join(retrieved_docs)

    # Verification prompt
    prompt = f"""
You are an AI verification analyst.

Your task is to verify whether the financial analysis
is fully supported by the retrieved evidence.

User Query:
{query}

Retrieved Evidence:
{evidence}

Generated Analysis:
{final_response}

Instructions:
- Identify unsupported claims
- Detect hallucinations
- Check whether conclusions are evidence-based
- Provide a verification summary
"""

    verification = ask_llm(prompt)

    print("\nVERIFICATION REPORT:\n")

    print(verification)

    # Save verification report
    state["verification_report"] = verification

    # Run evaluation
    evaluation = evaluate_workflow(
        state,
        verification
    )

    print("\nEVALUATION METRICS:\n")

    for key, value in evaluation.items():

        print(f"{key}: {value}")

    # Generate final report
    report = generate_report(
        state,
        evaluation
    )

    print("\nFINAL RESEARCH REPORT:\n")

    print(report)

    # Save research memory
    save_memory(state)
    return state