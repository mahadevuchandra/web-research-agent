import unittest
from dotenv import load_dotenv
load_dotenv()

from agents.content_analyzer import analyze_content

class TestContentAnalyzer(unittest.TestCase):
    def test_analyze_content(self):
        summary = analyze_content("Artificial intelligence is a branch of computer science...", "What is AI?")
        self.assertIsInstance(summary, str)

if __name__ == "__main__":
    unittest.main()
