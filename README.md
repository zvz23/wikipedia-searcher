# wikipedia-searcher

**wikipedia-searcher** is a library for scraping wikipedia information.

```python
>>> from wikisearch.wikisearcher import WikiSearcher
>>> searcher = WikiSearcher()
>>> searcher.search('React.js')
'React (also known as React.js or ReactJS) is a free and open-source front-end JavaScript library[3] for building user interfaces or UI components.'
```

If a search has has many options it returns a dictionary with a list of articles. You can can also pass the article to search.

```python
>>> from pprint import pprint
>>> search_result = searcher.search('The Hills')
>>> pprint(search_result)
>>> {'Places': [<wikisearch.article.ArticleLink object at 0x00000208A22EFAC0>,
            <wikisearch.article.ArticleLink object at 0x00000208A22EF7F0>,
            <wikisearch.article.ArticleLink object at 0x00000208A22EF6A0>,
            <wikisearch.article.ArticleLink object at 0x00000208A22EF400>,
            <wikisearch.article.ArticleLink object at 0x00000208A22EF3D0>,
            <wikisearch.article.ArticleLink object at 0x00000208A22EF370>],
 'Popular culture': [<wikisearch.article.ArticleLink object at 0x00000208A22EF940>,
                     <wikisearch.article.ArticleLink object at 0x00000208A22EF880>],
 'See also': [<wikisearch.article.ArticleLink object at 0x00000208A22EF340>,
              <wikisearch.article.ArticleLink object at 0x00000208A22EF8E0>]}
>>> article = search_result['Places'][0]
>>> article.name
'Santa Monica Mountains'
>>> article.link
'/wiki/Santa_Monica_Mountains'
>>> searcher.search(article)
'The Santa Monica Mountains is a coastal mountain range in Southern....'
```

## How to Install

Requests is available on PyPI:

```
$ pip install wikipedia-searcher
```
