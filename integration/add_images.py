from typing import List, Dict

from definitions_exemples.integration import get_definitions_and_examples_json
from figures.fetch_image import get_images_and_captions
from util.word_to_url import lookup_word
from util.dict_to_json import pretty_json
from util.extract_number import extract_number_from_string
from util.parse_html import get_html_content


def associate_figures_to_definitions(definitions: List[Dict], figures: List[Dict]) -> List[Dict]:
    result = definitions.copy()

    for figure in figures:
        definition_index = extract_number_from_string(figure['caption'])

        if definition_index:
            definitions[definition_index - 1]['image'] = figure

    return result


if __name__ == '__main__':
    url = lookup_word(word="entretenir")
    html = get_html_content(url=url)

    definitions = get_definitions_and_examples_json(html_content=html)
    print(pretty_json(dictionary=definitions))

    figures = get_images_and_captions(html_content=html)
    print(pretty_json(dictionary=figures))

    definitions_with_images = associate_figures_to_definitions(definitions=definitions, figures=figures)
    print(pretty_json(dictionary=definitions_with_images))
