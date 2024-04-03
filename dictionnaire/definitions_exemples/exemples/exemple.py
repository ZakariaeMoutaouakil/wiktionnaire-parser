from typing import List

from util.parse_html import parse_html


def get_examples(li_element: str) -> List[str] | None:
    # Parse the HTML using BeautifulSoup
    soup = parse_html(li_element)

    # Find the first li element
    first_li_element = soup.find("li")

    ul_element = first_li_element.find("ul")

    if ul_element:
        examples = []

        for example in ul_element.find_all("li"):
            text = ""
            emploi = example.find('span', class_='emploi')

            if emploi:
                i_element = emploi.find('i')

                if i_element:
                    text += i_element.get_text(strip=False) + " "

            i_element = example.find("i", recursive=False)

            if i_element:
                text += i_element.get_text(strip=False)
            else:
                alternate_example = example.find('span', class_='example')

                if alternate_example:
                    i_element = alternate_example.find("i")

                    if i_element:
                        text += i_element.get_text(strip=False)

            if text:
                examples.append(text)

        # Extract the text content of the li element
        return examples

    return None


if __name__ == "__main__":
    li_element_html = """
    <li><span class="emploi"><i>(<span class="texte"><a href="/wiki/Annexe:Glossaire_grammatical#P" title="Annexe:Glossaire grammatical">En particulier</a></span>)</i></span> Faire <a href="/wiki/subsister" title="subsister">subsister</a> en <a href="/wiki/fournir" title="fournir">fournissant</a> les choses <a href="/wiki/n%C3%A9cessaire" title="nécessaire">nécessaires</a>.
    <ul><li><i><b>Entretenir</b> un grand train, un grand équipage,</i> avoir beaucoup de valets, de chevaux, etc.</li>
    <li><i>Ils allumèrent des feux qu’ils <b>entretinrent</b> nuit et jour, et les hommes qu’on envoyait à la corvée du bois aux environs devaient tenir les loups en respect.</i> <span class="sources"><span class="tiret">— </span>(<a class="extiw" href="https://fr.wikipedia.org/wiki/H._G._Wells" title="w:H. G. Wells">H. G. Wells</a>, <i><a class="extiw" href="https://fr.wikipedia.org/wiki/La_Guerre_dans_les_airs" title="w:La Guerre dans les airs">La Guerre dans les airs</a></i>, 1908, traduction d’Henry-D. Davray et B. Kozakiewicz, <a class="extiw" href="https://fr.wikipedia.org/wiki/Mercure_de_France" title="w:Mercure de France">Mercure de France</a>, Paris, 1910, page 271 de l’édition de 1921)</span></li>
    <li><i><b>Entretenir</b> quelqu’un de linge, de vêtements.</i></li>
    <li><i>Il a de quoi s’<b>entretenir</b> honnêtement.</i></li>
    <li><i>Il s’entretient avec ce qu’il gagne, de ce qu’il gagne.</i></li>
    <li><i>Il s’entretient avec la pension que lui donne son père.</i></li>
    <li><i>Je donne tant à mon domestique pour s’<b>entretenir</b>.</i></li></ul></li>
    """
    print(get_examples(li_element=li_element_html))

    li_element_html = """
    <li><span class="emploi"><i>(<span class="texte">Pronominal</span>)</i></span> Se <a href="/wiki/conserver" title="conserver">conserver</a>, se <a href="/wiki/maintenir" title="maintenir">maintenir</a>.
    <ul><li><i>L’union ne <b>s’entretient</b> pas longtemps entre personnes qui ont des intérêts contraires.</i></li>
    <li><i>Parce que, formant une communauté soudée, ils <b>se sont entretenus</b> mutuellement dans l'illusion que les savants seraient plus forts que les militaires&#160;?</i> <span class="sources"><span class="tiret">—&#160;</span>(<a href="https://fr.wikipedia.org/wiki/Fr%C3%A9d%C3%A9ric_Pag%C3%A8s" class="extiw" title="w:Frédéric Pagès">Frédéric <span class="petites_capitales" style="font-variant: small-caps">Pagès</span></a>, <i>Pétards et farandoles</i>, <a href="https://fr.wikipedia.org/wiki/Le_Canard_encha%C3%AEn%C3%A9" class="extiw" title="w:Le Canard enchaîné">Le Canard enchaîné</a>, 18 mai 2016)</span></li></ul></li>
    <li><span class="emploi"><i>(<span class="texte">Pronominal</span>)</i></span> S’<a href="/wiki/exercer" title="exercer">exercer</a> pour se <a href="/wiki/maintenir" title="maintenir">maintenir</a> au même <a href="/wiki/degr%C3%A9" title="degré">degré</a> de <a href="/wiki/force" title="force">force</a>, de <a href="/wiki/savoir" title="savoir">savoir</a>.
    <ul><li><i>Il fait tous les jours des armes pour <b>s’entretenir</b> la main.</i></li></ul></li>
    """
    print(get_examples(li_element=li_element_html))

    li_element_html = """
    <li><span class="emploi"><i>(<span class="texte">Pronominal</span>)</i></span> <a href="/wiki/converser#fr" title="converser">Converser</a>, <a href="/wiki/discuter" title="discuter">discuter</a>.
    <ul><li><span class="example"><q><bdi lang="fr" class="lang-fr"><i>Nous <b>nous entretînmes</b> des moyens d'être l'un à l'autre.</i></bdi></q> <span class="sources"><span class="tiret">—&#160;</span>(<a href="https://fr.wikipedia.org/wiki/Abb%C3%A9_Pr%C3%A9vost" class="extiw" title="w:Abbé Prévost">Abbé Prévost</a>, <i>Histoire du chevalier des Grieux et de Manon Lescaut</i>,  1731, réédition 1967, Grenier-Flammarion, page 41)</span></span></li>
    <li><i>Tandis que nous <b>nous entretenions</b> amicalement avec ces bonnes gens, j’observais l’heureuse disposition du dressoir, de l’évier, des tablettes, où étaient rangés les pots et les assiettes.</i> <span class="sources"><span class="tiret">—&#160;</span>(<a href="https://fr.wikipedia.org/wiki/Johann_Wolfgang_von_Goethe" class="extiw" title="w:Johann Wolfgang von Goethe">Goethe</a>, <i>Campagne de France</i>, 1822&#160;; traduction française de Jacques Porchat, Paris&#160;: Hachette, 1889, page 93)</span></li>
    <li><span class="emploi"><span id="figuré"></span><i>(<span class="texte"><a href="/wiki/Annexe:Glossaire_grammatical#F" title="Annexe:Glossaire grammatical">Sens figuré</a></span>)</i></span> — <i>S’<b>entretenir</b> de ses propres pensées.</i></li>
    <li><span class="emploi"><span id="figuré"></span><i>(<span class="texte"><a href="/wiki/Annexe:Glossaire_grammatical#F" title="Annexe:Glossaire grammatical">Sens figuré</a></span>)</i></span> — <i>S’<b>entretenir</b> avec soi-même.</i></li></ul></li>
    """
    print(get_examples(li_element=li_element_html))
