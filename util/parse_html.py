import requests
from bs4 import BeautifulSoup


def get_html_content(url: str):
    response = requests.get(url)
    html_content = response.text

    # Parse the HTML using BeautifulSoup
    soup = parse_html(html_content)

    return str(soup)


def parse_html(html_string: str):
    return BeautifulSoup(html_string, "html.parser")
