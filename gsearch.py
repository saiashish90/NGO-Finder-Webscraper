import requests
from pprint import pprint
import pandas as pd
import re
import os

API_KEY = "AIzaSyCRyE5efidbgGrOmCSmcIqYOJS0PJrixsU"
SEARCH_ENGINE_ID = "8c2eebc9c4e912b0b"

df = pd.read_csv('./bangalore_ngo.csv')
urls = []

for ind in df.index:
    query = df['Name of NGO'][ind]
    page = 1
    start = (page - 1) * 10 + 1
    url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}"
    try:
        data = requests.get(url).json()
        search_items = data.get("items")
        for i, search_item in enumerate(search_items, start=1):
            title = search_item.get("title")
            link = search_item.get("link")
            x = re.search('facebook|globalgiving|deccanchronicle|zoominfo|linkedin|giveindia|changemakers+',link)
            if(x):
                continue
            else:
                print(ind)
                print("Title:", title, ' Index',i)
                print("URL:", link, "\n")
                urls.append(search_items[i-1].get("link"))
                break
    except:
         urls.append("no link")

links = pd.DataFrame(urls)
links.to_csv('./links_only')    
df['Link'] = urls
df.to_csv('./bangalore_ngo_link.csv',index = False)





