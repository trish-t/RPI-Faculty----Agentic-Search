"""
This file contains code related to the base functionality of the crawler at the base of the program.
It begins from a base URL and collects the department-specific links to crawl for faculty listing. From this point
it will visit each faculty page and invoke code to scrape the relevant information and continue onto the next.
"""

from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin, urlparse, urldefrag
from pathlib import Path

# GLOBAL VARIABLES #
PROJECT_ROOT = Path(__file__).resolve().parent.parent
IGNORE_FILE = PROJECT_ROOT / "Data" / "base_links_to_ignore.txt"

def load_links_to_ignore(filepath):
    '''
    @brief: reads in banned links fro a text file formatted as 1 link per line

    @param: filepath: the path to the file to read from
    '''
    banned_set = set()
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if(line == ""):
                continue
            banned_set.add(line)

    return list(banned_set)

def department_page_extract(page, url="https://faculty.rpi.edu/departments"):
    '''
    @brief: extracts outlinks from a scraped page.

    @param: url: base url to build off of
    @param: page: page that has already been scraped
    @return: list of outgoing links
    '''
    next_links = set()
    for a in page.find_all("a", href=True):
        href = a["href"].strip()
        if href.startswith(("mailto:", "tel:", "javascript:")):
            continue
        full_url = urljoin(url, href)
        full = urldefrag(full_url).url
        banned = load_links_to_ignore(IGNORE_FILE)
        if urlparse(full).scheme in ("http", "https"):
            if full not in banned:
                next_links.add(full)
                print(full)
    return list(next_links)

def init_crawl(url="https://faculty.rpi.edu/departments"):
    '''
    @brief: starts off crawling operations by defining a primary crawling space

    @param: url: base url for crawling, defaults to department page.
    @return: List of urls for the crawler to use
    '''

    # Initiate the crawl by grabbing base page
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
    except Exception as e:
        print("Error requesting base url: {e}")
        return False #flag for unexpected termination of the function

    # Save result to output file:
    base_html = "/Data/base_page.html"
    with open(base_html, "w", encoding="utf-8") as f:
        f.write(soup.prettify())

    print(f"Saved to {base_html}")
    department_page_extract(soup)

if __name__ == "__main__":
    init_crawl()