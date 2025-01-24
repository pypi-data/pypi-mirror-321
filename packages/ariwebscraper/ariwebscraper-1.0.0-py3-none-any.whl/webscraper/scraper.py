import requests
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, **headers):
        self.headers = headers or {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

    def fetch(self, url):
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            raise RuntimeError(f"Error: {e}")

    def extract(self, html, selector, method="css"):
        soup = BeautifulSoup(html, "html.parser")
        if method == "css" or "xpath":
            elements = soup.select(selector)
        else:
            raise ValueError("Invalid method. Use 'css' or 'xpath'.")
        return [element.get_text(strip=True) for element in elements]