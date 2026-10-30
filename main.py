from stats import count_words, count_chars, chars_dict_to_sorted_list

def main():
    path_to_file = "books/frankenstein.txt"
    book_text = get_book_text(path_to_file)
    characters = count_chars(book_text)
    sorted_characters = chars_dict_to_sorted_list(characters)

    print(f"Found {count_words(book_text)} total words")
    print(sorted_characters)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents



main()

