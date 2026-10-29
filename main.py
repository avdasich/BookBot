from stats import count_words

def main():
    path_to_file = "books/frankenstein.txt"
    book_text = get_book_text(path_to_file)

    print(book_text)
    print(f"Found {count_words(book_text)} total words")

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

main()

