from main import parse_html


def get_figures(html_content):
    # Parse the HTML using BeautifulSoup
    soup = parse_html(html_content)

    return soup.find_all("figure")


def get_image_and_caption(figure):
    result = {"src": figure.find("img")['src']}

    caption = figure.find("figcaption")

    for small in caption.find_all("small"):
        small.decompose()

    result["caption"] = caption.get_text(strip=False).strip()

    return result


def get_images_and_captions(url):
    return [get_image_and_caption(figure) for figure in get_figures(url)]
