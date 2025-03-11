# https://www.geeksforgeeks.org/web-scraping-from-wikipedia-using-python-a-complete-guide/

# import required modules
import requests
import pandas as pd

# get URL
url = 'https://www.imdb.com/chart/top/'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

page = requests.get(url, headers=headers)

# display status code
print(page.status_code)

# display scraped data
#print(page.content)

# import required modules
from bs4 import BeautifulSoup

# scrape webpage
soup = BeautifulSoup(page.content, 'html.parser')

# create a empty list for storing
# movie information
list = []

# Iterating over movies to extract
# each movie's details
items = soup.find_all(class_="cli-children")
for item in items:
    pre_title = item.find(class_="ipc-title__text").get_text()
    position = pre_title.split(".")[0]
    title = pre_title.split(".")[1].strip()
    metadata = item.find_all(class_="cli-title-metadata-item")
    year = metadata[0].get_text()
    duration = metadata[1].get_text()    
    rating = item.find(class_="ipc-rating-star--rating").get_text()
    votes = item.find(class_="ipc-rating-star--voteCount").get_text().strip(")")[2:]
    print(f"Position: {position}\nTitle: {title}\nYear: {year}\nDuration: {duration}\nRating: {rating}\nVotes: {votes}\n\n")
    data = {"position": position,
            "title": title,
            "year": year,
            "duration": duration,
            "rating": rating,
            "votes": votes
            }
    list.append(data)
    
df = pd.DataFrame(list)
df.to_csv('imdb_top_25_movies.csv',index=False)
    
    

