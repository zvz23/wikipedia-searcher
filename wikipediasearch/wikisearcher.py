from bs4 import BeautifulSoup
from .article import ArticleLink
from .wikiutil.wikiutil import *
import requests
from pprint import pprint
from more_itertools import peekable
class WikiSearcher:

    def __init__(self):            
        self.__URL_ROOT = 'https://en.wikipedia.org'
        self.__URL_SEARCH = 'https://en.wikipedia.org/wiki'
    
    def search(self, search):
        search_url = ''
        if isinstance(search, ArticleLink):
            search_url = self.__URL_ROOT + search.link
        else:
            search_replaced = search.replace(' ', '_')
            search_url = self.__URL_SEARCH + f'/{search_replaced}'
        raw_html = requests.get(search_url).text
        soup = BeautifulSoup(raw_html, 'lxml')
        body_content = soup.find('div', class_='mw-parser-output')
        if body_content is None:
            return 'Invalid search. No result.'
        if 'most often refers to:' not in soup.text and 'may also refer to:' not in soup.text and 'may refer to:' not in soup.text:
            wiki_clean_desc_recursive(body_content)
            return body_content.p.text
        else:
            wiki_clean_option(body_content)
            body_children = []
            for child in body_content.children:
                if child.name is not None and child.name not in ['style', 'h3']:
                    body_children.append(child)
            peekable_children = peekable(body_children)
            options = {}
            prev_key = None
            for child in peekable_children:
                peek_child = None
                try:
                    peek_child = peekable_children.peek()
                except StopIteration:
                    print('Iteration done.')
                if child.name == 'p' or child.name == 'h2':
                    prev_key = child.text.strip()
                    a_tag = child.find('a')
                    if a_tag is not None:
                        prev_key = f'{prev_key} (already a description select for more info.)'
                        options[prev_key] = []
                        article_link = ArticleLink(a_tag.attrs['title'], a_tag.attrs['href'])
                        options[prev_key].append(article_link)
                    else:
                        if peek_child.name  in ['p', 'h2']:
                            prev_key = f'{prev_key} (already a description)'
                            options[prev_key] = None


                else:
                    options[prev_key] = []
                    li_tags = child.find_all('li', recursive=False)
                    for li in li_tags:
                        a_tag = has_link(li)
                        if a_tag is None:
                            options[prev_key].append(li.text + ' (no other link)')
                        else:
                            article_link = ArticleLink(li.text, a_tag.attrs['href'])
                            options[prev_key].append(article_link)
            
            return options
                            

                        
                              
                
                
            
            
            
            

        
        
