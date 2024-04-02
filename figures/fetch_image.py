from typing import List, Dict

from util.word_to_url import lookup_word
from util.dict_to_json import pretty_json
from util.parse_html import parse_html, get_html_content


def get_figures(html_content: str) -> List:
    # Parse the HTML using BeautifulSoup
    soup = parse_html(html_content)

    return soup.find_all("figure")


def get_image_and_caption(figure) -> Dict:
    result = {"src": "https:" + figure.find("img")['src']}

    caption = figure.find("figcaption")

    for small in caption.find_all("small"):
        small.decompose()

    result["caption"] = caption.get_text(strip=False).strip()

    return result


def get_images_and_captions(html_content: str) -> List:
    return [get_image_and_caption(figure) for figure in get_figures(html_content)]


if __name__ == "__main__":
    url = lookup_word(word="verrou")
    html = get_html_content(url=url)
    figures = get_figures(html_content=html)
    print(figures)
    for figure in figures:
        print(get_image_and_caption(figure))
    print(pretty_json(get_images_and_captions(html)))

    url = lookup_word(word="entretenir")
    html = get_html_content(url=url)
    figures = get_figures(html_content=html)
    print(figures)
