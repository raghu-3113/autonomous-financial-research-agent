from datetime import datetime

import os


def generate_report(
    state,
    evaluation
):

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    report = f"""
# AUTONOMOUS FINANCIAL RESEARCH REPORT

Generated On:
{datetime.now()}

---

# USER QUERY

{state['query']}

---

# DETECTED INTENT

{state['intent']}

---

# RESEARCH PLAN

{state['plan']}

---

# TOOL OBSERVATIONS

"""

    # Add observations
    for obs in state["observations"]:

        report += f"""
## Tool Used:
{obs['tool']}

Status:
{obs.get('status', 'unknown')}

Output:
{obs['output']}

"""

    # Final synthesis
    report += f"""
---

# FINAL SYNTHESIS

{state['final_response']}

---

# VERIFICATION REPORT

{state['verification_report']}

---

# EVALUATION METRICS

"""

    # Metrics
    for key, value in evaluation.items():

        report += f"""
- {key}: {value}
"""

    report += "\n---\nEND OF REPORT\n"

    # Create folder
    output_dir = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../../outputs/reports"
        )
    )

    os.makedirs(
        output_dir,
        exist_ok=True
    )

    # Safe filename
    safe_query = (

    state["query"][:30]

    .replace(" ", "_")

    .replace("\n", "_")

    .replace("\r", "_")

    .replace("/", "_")

    .replace("\\", "_")

    .replace(":", "_")

    .replace("*", "_")

    .replace("?", "_")

    .replace('"', "_")

    .replace("<", "_")

    .replace(">", "_")

    .replace("|", "_")
)

    filename = (
        f"{safe_query}_{timestamp}.md"
    )

    filepath = os.path.join(
        output_dir,
        filename
    )

    # Save report
    with open(
        filepath,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(report)

    print("\nREPORT SAVED:\n")

    print(filepath)

    return report