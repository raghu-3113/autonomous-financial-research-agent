from rag.document_loader import load_documents
from rag.vector_store import create_vector_store
from rag.retriever import retrieve_documents

# Load documents once
chunks = load_documents()

# Create vector DB once
vectorstore = create_vector_store(chunks)

def retriever_node(state):

    query = state["query"]

    # Retrieve relevant docs
    results = retrieve_documents(vectorstore, query)

    retrieved_texts = []

    for doc in results:

        retrieved_texts.append(doc.page_content)

    print("\nRETRIEVED DOCUMENTS:\n")

    for i, text in enumerate(retrieved_texts):

        print(f"\n--- Retrieved {i+1} ---\n")

        print(text[:700])

    # Update workflow state
    state["retrieved_docs"] = retrieved_texts

    return state