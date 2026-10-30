from stats import count_words, count_chars, chars_dict_to_sorted_list

def main():
    path_to_file = "books/frankenstein.txt"
    book_text = get_book_text(path_to_file)
    characters = count_chars(book_text)
    total_words = count_words(book_text)
    sorted_characters = chars_dict_to_sorted_list(characters)
    print_report(path_to_file, total_words, sorted_characters)



def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def print_report(path_to_file ,total_words ,sorted_characters):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")

    for char, count in sorted_characters:
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")

main()

