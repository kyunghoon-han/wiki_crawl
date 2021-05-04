# wiki_crawl
Some wikipedia crawling module

## list_titles.py
`list_titles.py` produces a txt file of Wikipedia article ID, title pairs. 
This code is taken mostly from [this Stack Overflow page](https://stackoverflow.com/questions/24474288/how-to-obtain-a-list-of-titles-of-all-wikipedia-articles).
The file takes two terminal arguments:
1. `--language` or `-l`: language code (ex. `en` for English, `ko` for Korean), the default value is `ko`
2. `--filename` or `-f`: output filename (default: `list_titles.txt`)

## wiki_crawl.py
