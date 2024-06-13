import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.example.com/weather'
response = requests.get(url)
html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')
print(soup.prettify())  # Print the formatted HTML content