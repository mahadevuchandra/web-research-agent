import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Configure Gemini API key from environment variable for security
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load Gemini model (flash is faster and suitable for real-time applications)
model = genai.GenerativeModel("gemini-2.0-flash")

def analyze_content(text: str, query: str, context: str = "") -> str:
    """
    Uses Gemini to summarize the extracted content based on the user's query
    and optional conversational context.

    Args:
        text (str): Web content to analyze.
        query (str): User's research question.
        context (str): Prior conversation context or memory (optional).

    Returns:
        str: AI-generated summary or insight.
    """
    if not text.strip():
        return "No content extracted from the page."

    # Build the prompt for the Gemini model
    prompt = f"""
You are a research assistant. Use the context and the query below to extract relevant insights from the content.

Context from earlier conversation:
{context}

User Query: "{query}"

Content:
{text[:3000]}

Respond with a focused and clear answer.
"""

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Gemini analysis error: {e}")
        return "Error during AI analysis."
