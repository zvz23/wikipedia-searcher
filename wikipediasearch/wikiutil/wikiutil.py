from more_itertools import peekable
from bs4.element import NavigableString, Tag
from pprint import pprint

def wiki_clean_option(body_content):
    p_empty_elt = body_content.find('p', class_='mw-empty-elt')
    table_content = body_content.find('div', class_='tocright')
    edits = body_content.find_all('span', class_='mw-editsection')
    short_desc = body_content.find('div', class_='shortdescription nomobile noexcerpt noprint searchaux')
    style = body_content.find('style')
    note = body_content.find('div', role='note')
    tables = body_content.find_all('table')
    redirect = body_content.find('span', class_='mw-redirectedfrom')
    elements_to_clean = [table_content, tables, edits, short_desc, style, note, redirect, p_empty_elt]
    for element in elements_to_clean:
        if isinstance(element, list):
            for el in element:
                el.decompose()
        else:
            if element is not None:
                element.decompose()
def wiki_clean_option_p(filtered_body_content):
    prev_element = None
    for i, element in enumerate(filtered_body_content):
        if element.name == 'h2':
            prev_element = element.name
        elif element.name == 'p' and prev_element != None:
            filtered_body_content.pop(i)
            continue
        else:
            prev_element = None


def wiki_clean_desc(body_content):
    short_desc = body_content.find('div', class_='shortdescription nomobile noexcerpt noprint searchaux')
    id_note = body_content.find('div', role='note')
    class_note = body_content.find('div', class_='hatnote navigation-not-searchable')
    p = body_content.find('p', class_='mw-empty-elt')
    tables = body_content.find_all('table')
    coordinates = body_content.find('span', id='coordinates')
    div_site_sub = body_content.find('div', id='siteSub')
    elements_to_clean = [short_desc, id_note, class_note, p, coordinates, div_site_sub, tables ]

    for element in elements_to_clean:
        if element is not None:
            element.decompose()
        elif isinstance(element, list):
            for el in element:
                if el is not None:
                    el.decompose()

def wiki_clean_desc_recursive(body_content):
    for child in body_content.children:
        if child is None or (child.name == 'p' and len(child.attrs) == 0) or isinstance(child, NavigableString):
            pass
        else:
            child.decompose()

def has_link(tag):
    if not isinstance(tag, Tag):
        raise NameError('Invalid tag.')
    a_tag = tag.find('a')
    return a_tag




if __name__ == '__main__':
    pass
