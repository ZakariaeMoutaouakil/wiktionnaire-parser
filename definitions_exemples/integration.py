from definitions_exemples.definitions.definition import get_definition
from definitions_exemples.exemples.exemple import get_examples
from util.word_to_url import lookup_word
from util.dict_to_json import pretty_json
from util.parse_html import parse_html, get_html_content


def get_definitions_and_examples_html(html_content: str):
    # Parse the HTML using BeautifulSoup
    soup = parse_html(html_content)

    # Find the div element with the specified class
    div_element = soup.find("div", class_="mw-content-ltr mw-parser-output")

    # Find the first ol element within the div
    ol_element = div_element.find("ol")

    return [str(li_element) for li_element in ol_element.find_all("li", recursive=False)]


def get_definition_and_examples_json(li_element: str):
    exemples = get_examples(li_element)

    if exemples:
        return {"définition": get_definition(li_element), "exemples": exemples}

    return {"définition": get_definition(li_element)}


def get_definitions_and_examples_json(html_content: str):
    li_elements = get_definitions_and_examples_html(html_content)

    return [get_definition_and_examples_json(li_element) for li_element in li_elements]


if __name__ == "__main__":
    url_1 = lookup_word("entretenir")
    html_content_1 = get_html_content(url_1)
    print(get_definitions_and_examples_html(html_content_1))
    print(pretty_json(get_definitions_and_examples_json(html_content_1)))

    url_2 = lookup_word("verrou")
    html_content_2 = get_html_content(url_2)
    print(get_definitions_and_examples_html(html_content_2))
    print(pretty_json(get_definitions_and_examples_json(html_content_2)))
