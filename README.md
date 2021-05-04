# wiki_crawl
Some wikipedia crawling module

## list_titles.py
`list_titles.py` produces a txt file of Wikipedia article ID, title pairs. 
This code is taken mostly from [this Stack Overflow page](https://stackoverflow.com/questions/24474288/how-to-obtain-a-list-of-titles-of-all-wikipedia-articles).
The file takes two terminal arguments:
1. `--language` or `-l`: language code (ex. `en` for English, `ko` for Korean), the default value is `ko`
2. `--filename` or `-f`: output filename (default: `list_titles.txt`)

## wiki_crawl.py
`wiki_crawl.py` outputs a number of different text files to a designated output directory. The texts are taken from Wikipedia pages of title listed in an input list of titles (default: `list_titles.txt`).
The file takes three terminal arguments:
1. `--language` or `-l`: language code (as of above)
2. `--output` or `-o`: base output filename (if it's defined to be `./data/ko_article_`, as of the default case, a page of title "Python" would be saved as `./data/ko_article_Python.txt`)
3. `--input` or `-i`: the output of `list_titles.py`

## take_wikis.sh
Run both of the python files above.
