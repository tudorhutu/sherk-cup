import requests
from bs4 import BeautifulSoup
import random

def scrape_random_wiki_article():
    url = "https://en.wikipedia.org/wiki/Special:Random"
    response = requests.get(url=url)
    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.find(id="firstHeading")
    #print("Title: ", title.string)

    all_links = soup.find(id="bodyContent").find_all("a")
    random.shuffle(all_links)

    link_to_scrape = 0

    for link in all_links:
        # We are only interested in other wiki articles
        if link['href'].find("/wiki/") == -1: 
            continue

        # Use this link to scrape
        link_to_scrape = link
        break

    return "im mansplaining u about " + "https://en.wikipedia.org" + link_to_scrape['href']

#scrape_random_wiki_article()