from stats import count_words, count_chars

def main():
    path_to_file = "books/frankenstein.txt"
    book_text = get_book_text(path_to_file)
    characters = count_chars(book_text)

    print(book_text)
    print(f"Found {count_words(book_text)} total words")
    print(characters)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

main()

