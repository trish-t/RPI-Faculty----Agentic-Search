"""
This file holds functionality to collect faculty information from their RPI directory pages.
"""

from faculty import Faculty #custom class definition import
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin, urlparse, urldefrag
from pathlib import Path

TEST_URL = "https://faculty.rpi.edu/barbara-cutler"
PROJECT_ROOT = Path(__file__).resolve().parent.parent
REQUEST_HTML = PROJECT_ROOT / "Testing" / "test_extract.html"

def get_string(soup, selector):
    s = soup.select_one(selector)
    return s.get_text(strip=True) if s else None

def collect_page(url):
    """
    @brief: This function collects the html of the faculty page for processing

    @param: url: link to the page to request
    @returns: the html of the page
    """
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
    except Exception as e:
        print(f"Error requesting url: {e}")
        exit

    with open(REQUEST_HTML, "w", encoding="utf-8") as f:
        f.write(soup.prettify())

    return soup

def parse_page(url):
    soup = collect_page(url)

    #extracting the name
    name = get_string(soup, "h1.page-title span")
    firstname = name.split()[0]
    lastname = name.split()[1]

    #main department
    dept = get_string(soup, ".field--name-field-primary-department a")

    #


if __name__ == "__main__":
    parse_page(TEST_URL)