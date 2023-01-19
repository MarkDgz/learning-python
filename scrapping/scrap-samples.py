# Some Samples of Web Scrapping with BeautifulSoup
import requests
from bs4 import BeautifulSoup

url = "https://pixels.com/featured/2-elvis-presley-stars-on-art.html"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

# Use the 'prettify' function to view the HTML content of the page
print(soup.prettify())

# Get all links into webpage
for link in soup.find_all("a"):
    print(link.get("href"))
    
# Get all paragraphs into webpage
titles = soup.find_all("p")
for title in titles:
    print(title.text)

# All Web Text Including <Scripts>
text = soup.find_all(text=True)
print(" ".join(text))

# Extract information from the HTML using BeautifulSoup methods
title = soup.find("title").get_text()
print(title)
