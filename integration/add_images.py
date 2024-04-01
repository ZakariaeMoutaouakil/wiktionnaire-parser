from util.extract_number import extract_number_from_string


def associate_figures_to_definitions(definitions, figures):
    for figure in figures:
        definition_index = extract_number_from_string(figure['caption'])

        if definition_index:
            definitions[definition_index - 1]['image'] = figure