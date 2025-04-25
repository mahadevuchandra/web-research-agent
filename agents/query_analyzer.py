def analyze_query(query: str, history: list = None) -> dict:
    """
    Analyze a user's query to determine its type and extract keywords.

    Args:
        query (str): The user's research question.
        history (list, optional): List of previous user queries.

    Returns:
        dict: {
            "query_type": "factual" | "news" | "comparative",
            "keywords": List[str],
            "related_to_past": bool
        }
    """

    # Normalize query to lowercase for analysis
    query_lower = query.lower()

    # Classify the query type based on keywords
    if "latest" in query_lower or "news" in query_lower:
        query_type = "news"
    elif "compare" in query_lower or "vs" in query_lower:
        query_type = "comparative"
    else:
        query_type = "factual"

    # Remove common filler words (can be expanded or replaced with NLP stopword list)
    noise_words = {"what", "how", "the", "are", "and", "can", "you", "with", "for", "from", "this", "that", "will"}
    keywords = [
        word.strip(".,!?")
        for word in query_lower.split()
        if len(word) > 2 and word not in noise_words
    ]

    # Check for keyword overlap with past conversation history
    related_to_past = False
    if history:
        combined_history = " ".join(history).lower()
        related_to_past = any(word in combined_history for word in keywords)

    return {
        "query_type": query_type,
        "keywords": keywords,
        "related_to_past": related_to_past
    }
