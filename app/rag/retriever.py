def retrieve_documents(vectorstore, query):

    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3}
    )

    results = retriever.invoke(query)

    return results