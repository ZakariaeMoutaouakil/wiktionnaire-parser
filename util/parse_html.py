import requests
from bs4 import BeautifulSoup

from util.word_to_url import lookup_word


def get_html_content(url: str):
    response = requests.get(url)
    html_content = response.text

    # Parse the HTML using BeautifulSoup
    soup = parse_html(html_content)

    return str(soup)


def parse_html(html_string: str):
    return BeautifulSoup(html_string, "html.parser")


if __name__ == "__main__":
    url = lookup_word(word="entretenir")
    print(url)
    print(get_html_content(url))
