import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import urllib.robotparser
import hashlib

# In-memory cache to avoid redundant scraping in a session
_scrape_cache = {}

def can_scrape(url: str) -> bool:
    """
    Checks the site's robots.txt file to verify if scraping is allowed for the given URL.

    Args:
        url (str): The URL to check.

    Returns:
        bool: True if scraping is allowed or can't be determined, False if explicitly disallowed.
    """
    try:
        parsed_url = urlparse(url)
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
        robots_url = f"{base_url}/robots.txt"

        rp = urllib.robotparser.RobotFileParser()
        rp.set_url(robots_url)
        rp.read()
        return rp.can_fetch("*", url)
    except Exception as e:
        print(f"Robots.txt check failed for {url}: {e}")
        return True  # Allow scraping by default if robots.txt cannot be read

def scrape_text(url: str) -> str:
    """
    Scrapes the main textual content from a given URL if allowed by robots.txt.
    Uses caching to avoid redundant scraping.

    Args:
        url (str): The URL to scrape.

    Returns:
        str: Extracted textual content, or an empty string if disallowed or failed.
    """
    url_hash = hashlib.sha256(url.encode()).hexdigest()

    if url_hash in _scrape_cache:
        print("Using cached scrape result.")
        return _scrape_cache[url_hash]

    if not can_scrape(url):
        print(f"Scraping disallowed by robots.txt for {url}")
        return ""

    try:
        headers = {"User-Agent": "Mozilla/5.0 (compatible; WebResearchAgent/1.0)"}
        response = requests.get(url, headers=headers, timeout=7)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        content = " ".join(p.get_text() for p in paragraphs if p.get_text().strip())
        final_text = content.strip()

        _scrape_cache[url_hash] = final_text
        return final_text

    except Exception as e:
        print(f"Scraping error at {url}: {e}")
        return ""
