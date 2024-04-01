from util.parse_html import parse_html


def get_examples(li_element):
    # Parse the HTML using BeautifulSoup
    soup = parse_html(li_element)

    # Find the first li element
    li_element = soup.find("li")

    ul_element = li_element.find("ul")

    examples_html = [example.find("i") for example in ul_element.find_all("li", recursive=False)]

    # Extract the text content of the li element
    return [example.get_text(strip=False) for example in examples_html]
