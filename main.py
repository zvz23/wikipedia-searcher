from wikipediasearch.wikisearcher import WikiSearcher
from pprint import pprint
from sys import argv

search = WikiSearcher()

query = input('Search: ')
result = search.search(query)
if type(result) == str:
    print(result)
    exit()
for index, key in enumerate(result.keys()):
    print(f'{index + 1}. {key}')

option_one = int(input('Enter first option: '))
option_key = ''
for index, key in enumerate(result.keys()):
    if index  == option_one - 1:
        option_key = key
        break
for index, article in enumerate(result[option_key]):
        print(f'{index + 1}. {article.name}')


