"""
    The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that
    character appears only once in the original string, or ")" if that character appears more than once in the original
    string. Ignore capitalization when determining if a character is a duplicate.
"""


def duplicate_encode(word):
    input_str_lower = word.lower()
    char_count = {}
    for char in input_str_lower:
        char_count[char] = char_count.get(char, 0) + 1

    result_str = ""
    for char in word:
        if char_count[char.lower()] == 1:
            result_str += "("
        else:
            result_str += ")"

    return result_str

print(duplicate_encode("din"))