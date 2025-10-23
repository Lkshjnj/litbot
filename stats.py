def count_words_and_characters(filepath: str):
    with open(filepath, encoding="UTF-8") as f:
        file_contents = f.read()

    word_list = file_contents.split()
    char_dict = {}
    for char in file_contents.lower():
        char_dict[char] = char_dict.get(char, 0) + 1

    return len(word_list), char_dict    
        