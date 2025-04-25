import unittest
from dotenv import load_dotenv
load_dotenv()

from agents.synthesizer import synthesize_summaries

class TestSynthesizer(unittest.TestCase):
    def test_synthesize_summaries(self):
        summaries = ["AI is growing fast.", "It is used in many industries."]
        result = synthesize_summaries(summaries, "What is the future of AI?")
        self.assertIsInstance(result, str)

if __name__ == "__main__":
    unittest.main()
