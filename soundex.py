mapping = {'aeiouywh': '', 'bfpv': '1', 'cgjkqsxz': '2', 'dt': '3', 'l': '4', 'mn': '5', 'r': '6'}


def soundex(word):
    ...


def get_first_letter(word: str):
    return word[0]


def remove_upper_case_vowels(word_list: list[str]) -> list:
    return remove_given_chars(word_list, 'AEIOUWHY')


def remove_lower_case_vowels(word_list: list[str]) -> list:
    return remove_given_chars(word_list, 'aeiouwhy')


def remove_given_chars(word_list: list[str], chars_to_remove: str) -> list[str]:
    result = []
    for element in word_list:
        if element not in chars_to_remove:
            result.append(element)
    return result

