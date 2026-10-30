
def count_words(file_contents):
    num_words = file_contents.split()
    return len(num_words)

def count_chars(file_contents):
    char_count = {}
    for char in file_contents:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(characters: tuple[str, int]) -> int:
    return characters[1]

def chars_dict_to_sorted_list(count_chars: dict[str, int]) -> list[tuple[str, int]]:
    sorted_chars = []
    for char in count_chars:
        sorted_chars.append((char, count_chars[char]))
    sorted_chars = sorted(sorted_chars, key=sort_on, reverse=True)
    return sorted_chars
