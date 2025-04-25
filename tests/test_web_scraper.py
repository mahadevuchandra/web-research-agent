import unittest
from agents.web_scraper import scrape_text

class TestWebScraper(unittest.TestCase):
    def test_scrape_text(self):
        url = "https://en.wikipedia.org/wiki/Artificial_intelligence"
        text = scrape_text(url)
        self.assertIsInstance(text, str)
        self.assertGreater(len(text), 100)

if __name__ == "__main__":
    unittest.main()
