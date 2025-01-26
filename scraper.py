import requests
from bs4 import BeautifulSoup

def scrape_text_to_file(url, output_file):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text(strip=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text)

scrape_text_to_file("https://www.ewor.com/?sc=EW&ssc=Pre-Idea-Top&sm=Direct", "output.txt")
