import unittest
from src.webscraper import Scraper


class TestScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = Scraper()

    def test_fetch(self):
        url = "https://www.example.com"
        html = self.scraper.fetch(url)
        self.assertIsInstance(html, str)

    def test_extract(self):
        html = "<h1>Hello, World!</h1>"
        data = self.scraper.extract(html, "h1")
        self.assertEqual(data, ["Hello, World!"])


if __name__ == "__main__":
    unittest.main()
