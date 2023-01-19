# Program:     scrap-gen-json-ld.py
# Description: Exercise about scrap data and generating information into JSON-LD format
# Changes: 
# 1. New Program
# Licence: MIT
# Dev status: Latest Stable Version 1.0.0

# # Required libraries
# python programs to support file and directory functions
import os
import sys

#Parameters
if len(sys.argv):
    text = sys.argv[1]
else:
    print("Put the URL Text as Paremeter, poner la URL o Web Link como paramentro")

#Exercise about scrap data and generating information into JSON-LD format
import requests
from bs4 import BeautifulSoup
import json

#url = "https://www.example.com"
url = text
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
