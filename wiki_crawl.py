import argparse, csv
import wikipediaapi
from tqdm import tqdm

parser = argparse.ArgumentParser(description='Fetches texts from Wikipedia')
parser.add_argument('--language','-l',dest='lang',
                    help="Language of the Wikipedia articles",
                    default='ko',
                    type=str)
parser.add_argument('--output','-o', dest='output',
                    help="Base filename to be output",
                    default='./data/ko_article_')
parser.add_argument('--input','-i', dest='input',
                    help="Input filename",
                    default='list_titles.txt')

args = parser.parse_args()

in_f = args.input
out_base = args.output
lang = args.lang

wiki = wikipediaapi.Wikipedia(lang)

with open(in_f, "r") as f:
    titles = [row[1] for row in csv.reader(f,delimiter=";")]
    for a_title in tqdm(titles):
        page = wiki.page(a_title)
        if page.exists():
            filename = out_base + page.title
            filename = filename + ".txt"
            with open(filename,"w") as fw:
                fw.write(page.text)
        else:
            print("The page on %f does not exist!" %(a_title))
