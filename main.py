import sys
from stats import get_num_words, get_num_each_char, sort_dict

def get_book_text(book_path):
    with open(book_path, "r", encoding="utf-8") as file:
        # file is a file object
        print(f"Analyzing book found at: {book_path}...")
        file_contents = file.read()
        return file_contents

def main(book_path):
    print("============ BOOKBOT ============")
    book_text = get_book_text(book_path)
    amounts = get_num_each_char(book_text)
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_text)} total words")
    print("------- Character Count ---------")
    amounts = sort_dict(amounts)
    for char, count in amounts.items():
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    main(sys.argv[1])