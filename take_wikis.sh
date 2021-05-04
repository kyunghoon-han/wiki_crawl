mkdir -p data
echo "Take article titles in Wikipedia"
python3 list_titles.py
echo "Save the text data of each article"
python3 wiki_crawl.py
