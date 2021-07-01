from wikipediasearch.wikisearcher import WikiSearcher
from wikipediasearch.wikiutil.report import *
import argparse

parser = argparse.ArgumentParser(
    description='Search information from Wikipedia')
parser.add_argument('-s', type=str, help='Search string')
parser.add_argument('-main', type=str, help='Search option main')
parser.add_argument('-sub', type=int, help='Search option sub')
args = parser.parse_args()


search = WikiSearcher()
if args.s is None or len(args.s) < 0:
    print('Invalid search.')

result = search.search(args.s)
print('Search result: ')
if type(result) == str:
    print(result)
else:
    if args.main is not None:
        try:
            sub_options = result[args.main]
            if args.sub is not None:
                sub_option_found = None
                for index, sub_option in enumerate(sub_options):
                    if args.sub - 1 == index:
                        sub_option_found = sub_option
                        break
                if sub_option_found is not None:
                    sub_result = search.search(sub_option_found)
                    if type(sub_result) == str:
                        print(sub_result)
                    else:
                        print(stringify_main_options(sub_result))
                        print(f'Next time search {sub_option_found.name}')
                else:
                    raise KeyError
            else:
                print(stringify_sub_options(result, args.main))
        except KeyError:
            print('Key Error: Invalid option')
    else:
        print(stringify_main_options(result))
