import requests
from bs4 import BeautifulSoup

# Send an HTTP request to the website
response = requests.get('http://example.com')

# Parse the HTML or XML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the data you want to scrape
data = soup.find_all('p')

# Print the data
print(data)
