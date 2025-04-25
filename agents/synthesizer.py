import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Securely configure the Gemini API key from environment variable
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load Gemini model (flash version for speed and low latency)
model = genai.GenerativeModel("gemini-2.0-flash")

def synthesize_summaries(summaries: list[str], query: str) -> str:
    """
    Synthesizes multiple content summaries into one cohesive final answer.

    Args:
        summaries (list): List of AI-generated summaries from each URL.
        query (str): The original user query.

    Returns:
        str: Final, synthesized response.
    """
    combined = "\n\n---\n\n".join(summaries)

    prompt = f"""
You are a professional research assistant. Your task is to synthesize insights from multiple articles into a single concise, unbiased report.

User Query: "{query}"

Article Summaries:
{combined[:12000]}

Now create a final response that:
- Answers the user's query clearly
- Removes repetition
- Resolves any conflicting points (if found)
- Includes helpful insights, not fluff

Return only the final summary.
"""

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Synthesis error: {e}")
        return "Error during synthesis."
