
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