from util.parse_html import parse_html


def get_examples(li_element):
    # Parse the HTML using BeautifulSoup
    soup = parse_html(li_element)

    # Find the first li element
    li_element = soup.find("li")

    ul_element = li_element.find("ul")

    if ul_element:
        examples_html = [example.find("i") for example in ul_element.find_all("li", recursive=False)]

        # Extract the text content of the li element
        return [example.get_text(strip=False) for example in examples_html]

    return None


if __name__ == "__main__":
    li_element = """
    <li><span class="emploi"><i>(<span class="texte"><a href="/wiki/Annexe:Glossaire_grammatical#P" title="Annexe:Glossaire grammatical">En particulier</a></span>)</i></span> Faire <a href="/wiki/subsister" title="subsister">subsister</a> en <a href="/wiki/fournir" title="fournir">fournissant</a> les choses <a href="/wiki/n%C3%A9cessaire" title="nécessaire">nécessaires</a>.
    <ul><li><i><b>Entretenir</b> un grand train, un grand équipage,</i> avoir beaucoup de valets, de chevaux, etc.</li>
    <li><i>Ils allumèrent des feux qu’ils <b>entretinrent</b> nuit et jour, et les hommes qu’on envoyait à la corvée du bois aux environs devaient tenir les loups en respect.</i> <span class="sources"><span class="tiret">— </span>(<a class="extiw" href="https://fr.wikipedia.org/wiki/H._G._Wells" title="w:H. G. Wells">H. G. Wells</a>, <i><a class="extiw" href="https://fr.wikipedia.org/wiki/La_Guerre_dans_les_airs" title="w:La Guerre dans les airs">La Guerre dans les airs</a></i>, 1908, traduction d’Henry-D. Davray et B. Kozakiewicz, <a class="extiw" href="https://fr.wikipedia.org/wiki/Mercure_de_France" title="w:Mercure de France">Mercure de France</a>, Paris, 1910, page 271 de l’édition de 1921)</span></li>
    <li><i><b>Entretenir</b> quelqu’un de linge, de vêtements.</i></li>
    <li><i>Il a de quoi s’<b>entretenir</b> honnêtement.</i></li>
    <li><i>Il s’entretient avec ce qu’il gagne, de ce qu’il gagne.</i></li>
    <li><i>Il s’entretient avec la pension que lui donne son père.</i></li>
    <li><i>Je donne tant à mon domestique pour s’<b>entretenir</b>.</i></li></ul></li>
    """
    print(get_examples(li_element))
