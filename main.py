from stats import count_words_and_characters

def main():
    word_count, char_count = count_words_and_characters("./books/frankenstein.txt")
    print(f"found {word_count} in the text\n")
    print(f"the character count is as follows \n {char_count}")

if __name__ == "__main__":
    main()