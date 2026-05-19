import streamlit as st

from workflow.graph_builder import build_graph

# Page config
st.set_page_config(
    page_title="Financial Research Agent",
    layout="wide"
)

# Title
st.title(
    "Autonomous Financial Research Agent"
)

st.write(
    "AI-powered autonomous financial analysis system"
)

# Sidebar
st.sidebar.header("Research Settings")

query = st.sidebar.text_area(
    "Enter Financial Research Query",
    height=120
)

# Run button
run_button = st.sidebar.button(
    "Run Research"
)

# Execute workflow
if run_button and query:

    graph = build_graph()

    initial_state = {

        "query": query,

        "intent": "",

        "plan": "",

        "observations": [],

        "retrieved_docs": [],

        "final_response": "",

        "verification_report": ""
    }

    with st.spinner(
        "Running autonomous workflow..."
    ):

        result = graph.invoke(
            initial_state
        )

    # Sidebar outputs
    st.sidebar.subheader(
        "Detected Intent"
    )

    st.sidebar.success(
        result["intent"]
    )

    # Main layout
    tab1, tab2, tab3, tab4 = st.tabs([

        "Research Plan",

        "Tool Observations",

        "Final Analysis",

        "Verification"
    ])

    # TAB 1
    with tab1:

        st.subheader(
            "Research Plan"
        )

        st.write(result["plan"])

    # TAB 2
    with tab2:

        st.subheader(
            "Tool Observations"
        )

        for obs in result["observations"]:

            with st.expander(
                f"{obs['tool']} ({obs['status']})"
            ):

                st.write(obs["output"])

    # TAB 3
    with tab3:

        st.subheader(
            "Final Synthesis"
        )

        st.write(
            result["final_response"]
        )

    # TAB 4
    with tab4:

        st.subheader(
            "Verification Report"
        )

        st.write(
            result["verification_report"]
        )

    st.success(
        "Workflow Completed"
    )