import pdfplumber
from tqdm import tqdm
import sys

def count_words_and_characters(filepath: str):
    file_contents = ""
    try:
        if ".pdf" in filepath:
            with pdfplumber.open(filepath) as pdf:
                total_pages = len(pdf.pages)
                for page_num in tqdm(range(total_pages), desc="Reading PDF", unit="page"):
                    page = pdf.pages[page_num]
                    file_contents += page.extract_text()
        else:
            with open(filepath, encoding="UTF-8") as f:
                file_contents = f.read()

    except Exception as e:
        print(f"{str(e)}\n [-] Incorrect file type\n [+]Usage: either provide a pdf (with .pdf extension) or a text file")
        sys.exit(-1)
    word_list = file_contents.split()
    char_dict = {}
    for char in file_contents.lower():
        char_dict[char] = char_dict.get(char, 0) + 1

    return len(word_list), char_dict    

def sort_on(items):                    # helper function to sort the list of dictionaries returned by char_and_report function.
    return items['num']

def char_for_report(char_dict: dict):
    organized_list = [{'char': key, 'num': value} for key, value in char_dict.items()]
    organized_list.sort(reverse=True, key=sort_on)
    return organized_list