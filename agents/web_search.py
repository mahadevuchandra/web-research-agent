def search_web(query: str, num_results: int = 5) -> list:
    """
    Simulates a web search by returning mock URLs for the given query.
    Designed for demonstration purposes where actual API usage is restricted.

    Args:
        query (str): The search query.
        num_results (int): Number of results to return (default is 5).

    Returns:
        list: A list of mock URLs related to the query.
    """

    # Dictionary of mock search results based on keyword categories
    mock_links = {
        "ai": [
            "https://www.ibm.com/topics/artificial-intelligence",
            "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "https://builtin.com/artificial-intelligence"
        ],
        "climate change": [
            "https://climate.nasa.gov/",
            "https://www.un.org/en/climatechange",
            "https://en.wikipedia.org/wiki/Climate_change"
        ],
        "python programming": [
            "https://realpython.com/",
            "https://www.python.org/about/gettingstarted/",
            "https://docs.python.org/3/"
        ]
    }

    # Return mock results if a matching keyword is found in the query
    query_lower = query.lower()
    for keyword, urls in mock_links.items():
        if keyword in query_lower:
            return urls[:num_results]

    # Fallback generic search-related links
    return [
        "https://en.wikipedia.org/wiki/Web_search_engine",
        "https://www.techtarget.com/whatis/definition/search-engine",
        f"https://www.google.com/search?q={query.replace(' ', '+')}"
    ][:num_results]
