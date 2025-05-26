import json
import requests
from bs4 import BeautifulSoup

# Replace this with the actual URL
url = 'https://travelwithlanguages.com/blog/most-common-swedish-words.html'

# Fetch the page
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the ordered list with id 'main-list'
ol = soup.find('ol', id='main-list')
if not ol:
    raise ValueError("Could not find <ol id='main-list'>")

words = []

# Loop through each <li> item in the list
for li in ol.find_all('li'):
    rank_tag = li.find('span', class_='rank-number')
    word_divs = li.find_all('div')

    if len(word_divs) < 3 or not rank_tag:
        continue

    rank = int(rank_tag.text.strip().strip('.'))
    word = word_divs[0].text.strip()
    pos = word_divs[1].text.strip().strip('[]')
    definition = word_divs[2].text.strip().strip('()')

    words.append({
        "rank": rank,
        "word": word,
        "type": pos,
        "definition": definition
    })

# Save to JSON file
with open('swedish_common_words.json', 'w', encoding='utf-8') as f:
    json.dump(words, f, ensure_ascii=False, indent=2)

print("✅ Saved 1000 common words to 'swedish_common_words.json'")