def count_words_and_characters(filepath: str):
    with open(filepath, encoding="UTF-8") as f:
        file_contents = f.read()

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