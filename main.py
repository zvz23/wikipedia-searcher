from wikipediasearch.wikisearcher import WikiSearcher
from pprint import pprint

search = WikiSearcher()

query = input('Search: ')
result = search.search(query)
if type(result) == str:
    print(result)
    exit()
#for index, key in enumerate(result.keys()):
#    print(f'{index + 1}. {key}')
pprint(result)