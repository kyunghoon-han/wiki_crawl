import sys
from simplemediawiki import MediaWiki
import argparse

parser = argparse.ArgumentParser(description='Retrieves a list of wikipedia pages in a given language')
parser.add_argument('--language', '-l',dest='lang',
                    help='Language of the wikipedia articles',
                    default='ko',
                    type=str)
parser.add_argument('--filename', '-f',dest='filename',
                    help='Output filename',
                    default='list_titles.txt')

args = parser.parse_args()

lang_val = args.lang
filename = args.filename

wiki_url = "https://"
wiki_url = wiki_url + lang_val
wiki_url = wiki_url + ".wikipedia.org/w/api.php"

wiki = MediaWiki(wiki_url)

output_file = open(filename,"w")

continue_param = ''
request_obj = {}
request_obj['action'] = 'query'
request_obj['list'] = 'allpages'
request_obj['aplimit'] = 'max'
request_obj['apnamespace'] = '0'

page_list = wiki.call(request_obj)
pages_in_query = page_list['query']['allpages']

for each_page in pages_in_query:
    page_ID = each_page['pageid']
    title = each_page['title']
    write_str = str(page_ID)+"; " + title + "\n"
    output_file.write(write_str)

num_queries = 1

while len(page_list['query']['allpages'])>0:
    request_obj['apcontinue'] = page_list["continue"]["apcontinue"]
    page_list = wiki.call(request_obj)

    pages_in_query = page_list['query']['allpages']

    for each_page in pages_in_query:
        page_ID = each_page['pageid']
        title = each_page['title']#.encode('utf-8')
        write_str = str(page_ID) + "; " + title + "\n"
        output_file.write(write_str)

    num_queries += 1
    if num_queries % 100 == 0:
        print("Done with queries -- ", num_queries)
        print(num_queries)

output_file.close()
