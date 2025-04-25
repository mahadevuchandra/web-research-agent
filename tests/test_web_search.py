import unittest
from agents.web_search import search_web

class TestWebSearch(unittest.TestCase):
    def test_search_web(self):
        results = search_web("python programming")
        self.assertIsInstance(results, list)
        self.assertTrue(any("python" in url.lower() for url in results))

if __name__ == "__main__":
    unittest.main()
