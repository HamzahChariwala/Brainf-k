import requests
from bs4 import BeautifulSoup

def scrape_text_to_file(url, output_file):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text(strip=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text)

def text_to_ascii(input_file, output_file=None):

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    words = content.split()

    lines = []
    for word in words:
        ascii_codes = [str(ord(c)) for c in word]
        line = " ".join(ascii_codes)
        lines.append(line)
    if output_file is None:
        for line in lines:
            print(line)
    else:
        with open(output_file, 'w', encoding='utf-8') as f_out:
            f_out.write("\n".join(lines))



text_to_ascii("output.txt", "ascii_codes.txt")


# scrape_text_to_file("https://www.ewor.com/?sc=EW&ssc=Pre-Idea-Top&sm=Direct", "output.txt")
