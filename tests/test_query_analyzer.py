import unittest
from agents.query_analyzer import analyze_query

class TestQueryAnalyzer(unittest.TestCase):
    def test_analyze_query(self):
        result = analyze_query("Tell me about artificial intelligence.")
        self.assertIn("keywords", result)
        self.assertIsInstance(result["keywords"], list)
        self.assertGreater(len(result["keywords"]), 0)

if __name__ == "__main__":
    unittest.main()
