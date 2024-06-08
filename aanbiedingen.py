#! /usr/bin/python3

import requests
from lxml.html import fromstring


page = requests.get("http://localhost")

# print(page.request.body)
tree = fromstring(page.text)

elements = tree.xpath('//a')  # Replace with your XPath expression

# Iterate over the selected elements
for element in elements:
    title = element.get('title')
    if not title or "aanbiedingen" in title or "Aanbiedingen" in title:
        continue
    # Access title properties or extract data
    print(title)