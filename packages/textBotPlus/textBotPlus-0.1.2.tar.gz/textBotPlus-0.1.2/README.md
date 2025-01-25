# textBotPlus

A utility package for processing JSON data and extracting text from HTML.

## Installation

You can install this package via pip:

```bash
pip install textBotPlus

Example 1: 

from textBotPlus import get_json_text

json_data = {"user": {"name": "John", "age": 30}}
keys = ["user", "name"]
result = get_json_text(json_data, keys)
print(result)  # Output: "John"

Example 2

from textBotPlus import get_selector_text
from bs4 import BeautifulSoup

html = '<html><body><p id="paragraph">Hello, world!</p></body></html>'
soup = BeautifulSoup(html, 'html.parser')

result = get_selector_text(soup, css_selector="#paragraph")
print(result)  # Output: "Hello, world!"
