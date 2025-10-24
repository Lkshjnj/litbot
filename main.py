from stats import count_words_and_characters, char_for_report
import sys

def main():

    if len(sys.argv) != 2:
        print("[-] Usage: python3 main.py <filepath>")
        sys.exit(1)

    print("==================== BOOKBOT =========================\n\n")
    print("==================== Word Count ======================\n")
    word_count, char_count = count_words_and_characters(sys.argv[1])
    print(f"found {word_count} in the text\n")
    # print(f"the character count is as follows \n {char_for_report(char_count)}")
    print("====================== Character Count ========================")
    for item in char_for_report(char_count):
        if item['char'].isalpha():
            print(f"{str(item["char"])} : {str(item["num"])}")
    print("======================= END ============================")
if __name__ == "__main__":
    main()