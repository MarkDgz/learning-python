#Exercise about scrap data and generating information into JSON-LD format
import requests
from bs4 import BeautifulSoup
import json

url = "https://www.example.com"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Extract information from the HTML using BeautifulSoup methods
title = soup.find("title").get_text()
links = [link.get("href") for link in soup.find_all("a")]

# Convert the extracted information into JSON-LD format
data = {
    "@context": "http://schema.org",
    "@type": "WebPage",
    "url": url,
    "name": title,
    "hasPart": [{"@type": "WebPage", "url": link} for link in links]
}

# Save the JSON-LD data to a file
with open("output.jsonld", "w") as f:
    json.dump(data, f)
