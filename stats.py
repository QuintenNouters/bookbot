def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_each_char(text):
    char_count = {}
    for char in text:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_dict(d):
    return dict(sorted(d.items()))