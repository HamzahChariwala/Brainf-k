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

def best_single_value_code(m):

    best_code = ">" + ("+" * m)
    best_len = 1 + m

    for a in range(2, m):
        if m % a == 0:
            b = m // a
            loop_code = (
                "+" * a  
                + "[>"
                + "+" * b  
                + "<-]"
                + ">"
            )
            code_len = a + b + 6
            if code_len < best_len:
                best_len = code_len
                best_code = loop_code

    return str(best_code)


def ascii_to_bf_optimised(n):

    best_n_code = best_single_value_code(n)
    best_code = best_n_code
    best_length = len(best_n_code)

    for m in range(1, 256):
        code_for_m = best_single_value_code(m)
        diff = abs(n - m)
        candidate_length = len(code_for_m) + diff

        if candidate_length < best_length:
            if n > m:
                difference_code = "+" * (n - m)
            else:
                difference_code = "-" * (m - n)
            candidate_code = code_for_m + difference_code
            best_code = candidate_code
            best_length = candidate_length

    return str(best_code)


def parse_ascii_file_to_array(input_file):
    result = []
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            values = list(map(int, line.split()))
            result.append(values)
    return result

def convert_ascii_to_bf(input_file, output_file):
    array = parse_ascii_file_to_array(input_file)
    bf_string = ""
    for line in array:
        char_count = len(line)
        for value in line:
            code = ascii_to_bf_optimised(value)
            bf_string = bf_string + code + "." + "[-]<"
        bf_string = bf_string + "++++++++[>++++<-]>.<"
    with open(output_file, 'w', encoding='utf-8') as f_out:
        f_out.write(bf_string)


if __name__ == "__main__":
    scrape_text_to_file("https://www.ewor.com/?sc=EW&ssc=Pre-Idea-Top&sm=Direct", "text_handling/output.txt")
    text_to_ascii("text_handling/output.txt", "text_handling/ascii_codes.txt")
    convert_ascii_to_bf("text_handling/ascii_codes.txt", "brainf--k_code.bf")









