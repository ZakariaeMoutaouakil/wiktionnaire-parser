from typing import List, Dict, Union

from dictionnaire.definitions_exemples.integration import get_definitions_and_examples_json
from dictionnaire.figures.fetch_image import get_images_and_captions
from util.dict_to_json import pretty_json
from util.extract_number import extract_number_from_string
from util.parse_html import get_html_content
from util.word_to_url import lookup_word


def associate_figures_to_definitions(definitions: List[Dict[str, Union[str, List[str]]]],
                                     figures: List[Dict[str, str]]):
    result: List[Dict[str, Union[str, List[str], Dict[str, str]]]] = definitions.copy()

    for figure in figures:
        definition_index = extract_number_from_string(figure['caption'])

        if definition_index:
            result[definition_index - 1]['image'] = figure

    return result


def dictionary(word: str) -> Dict[str, List[Dict[str, Union[str, List[str], Dict[str, str]]]]]:
    link = lookup_word(word=word)
    html = get_html_content(url=link)
    defs = get_definitions_and_examples_json(html_content=html)
    figs = get_images_and_captions(html_content=html)
    return {word: associate_figures_to_definitions(definitions=defs, figures=figs)}


if __name__ == '__main__':
    for w in ["entretenir", "verrou", "manque"]:
        print(pretty_json(dictionary(w)))
