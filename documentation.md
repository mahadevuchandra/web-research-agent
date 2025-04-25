
# documentation.md  
## Web Research Agent – Architecture & Design Explanation

---

### 1. Agent Structure

The Web Research Agent follows a modular, pipeline-based architecture:

```
User Query
   ↓
[Query Analyzer]
   ↓
[Web Search Engine]
   ↓
[Web Scraper]
   ↓
[Content Analyzer]
   ↓
[Synthesizer]
   ↓
Final Answer
```

**Modules:**

- `main.py`: Orchestrates the flow and provides the UI via Streamlit.
- `agents/query_analyzer.py`: Extracts key topics/keywords from user input.
- `agents/web_search.py`: Finds relevant links using a mock search (replacing SerpAPI).
- `agents/web_scraper.py`: Extracts main textual content using BeautifulSoup.
- `agents/content_analyzer.py`: Summarizes individual articles using the Gemini model.
- `agents/synthesizer.py`: Synthesizes all summaries into a coherent final response.

---

### 2. Prompt & Instruction Design

#### **Prompt Strategy:**
Prompts are structured with **clear task roles** and **explicit constraints**.  
We follow a few-shot instruction format like:

```
You are a professional research assistant...
- Provide unbiased synthesis
- Remove repetition
- Resolve contradictions
- Only return final summary
```

This ensures consistency and reliability when aggregating multiple sources.

Each summary step is query-aware: the content analyzer and synthesizer are both given the original user query to ensure focus and relevance.

---

### 3. External Tool Integration

| Tool               | Purpose                                | How It's Used                          |
|--------------------|----------------------------------------|----------------------------------------|
| **Google Gemini**  | LLM-based content summarization        | Via `google.generativeai` package and `.env` API key |
| **BeautifulSoup4** | HTML parsing and text extraction       | For scraping web content               |
| **Streamlit**      | Interactive frontend for chat & display| Provides UI and session state          |

#### Environment Variables
- `.env` file securely stores sensitive values like:
  - `GOOGLE_API_KEY` for Gemini
- Loaded automatically via `python-dotenv`

---

### 4. Error Handling

Each module is built with try-except blocks and graceful fallbacks:

| Module             | Common Errors Handled                  | Fallback Behavior                      |
|--------------------|----------------------------------------|----------------------------------------|
| Web Scraper        | Invalid URL / timeouts / HTTP errors   | Skips the link and logs a message      |
| Gemini Summarizer  | API failure / token limit exceeded     | Returns error message in UI gracefully |
| Web Search         | No results found                       | Returns empty list with a notice       |

All exceptions are caught and logged without crashing the app. The chatbot continues functioning even with partial results.

---

### 5. Testing Strategy

- `tests/` folder includes unit tests for core agents (query and content analyzer, scraper, search, summarizer).
- Uses dummy prompts and mocked outputs to validate logic.
