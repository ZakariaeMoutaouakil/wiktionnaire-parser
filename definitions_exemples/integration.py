from definitions_exemples.definitions.definition import get_definition
from definitions_exemples.exemples.exemple import get_examples
from util.parse_html import parse_html


def get_definitions_and_examples_html(html_content: str):
    # Parse the HTML using BeautifulSoup
    soup = parse_html(html_content)

    # Find the div element with the specified class
    div_element = soup.find("div", class_="mw-content-ltr mw-parser-output")

    # Find the first ol element within the div
    ol_element = div_element.find("ol")

    return [str(li_element) for li_element in ol_element.find_all("li", recursive=False)]


def get_definition_and_examples_json(li_element):
    return {"definition": get_definition(li_element), "exemples": get_examples(li_element)}


def get_definitions_and_examples_json(url):
    li_elements = get_definitions_and_examples_html(url)

    return [get_definition_and_examples_json(li_element) for li_element in li_elements]
