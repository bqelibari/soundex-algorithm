from typing import List

mapping = {'aeiouywh': '', 'bfpv': '1', 'cgjkqsxz': '2', 'dt': '3', 'l': '4', 'mn': '5', 'r': '6'}


def soundex(word):
    ...


def get_first_letter(word: str):
    return word[0]


def remove_upper_and_lower_case_vowels(char_list: list[str]) -> list:
    return remove_given_chars(char_list, 'AEIOUWHYaeiouwhy')


def remove_given_chars(word_list: list[str], chars_to_remove: str) -> list[str]:
    result: list[str] = []
    for element in word_list:
        if element not in chars_to_remove:
            result.append(element)
    return result


def replace_given_consonants_with_value(char_list: list[str], consonants: str, value_as_string: str) -> list[str]:
    for idx, element in enumerate(char_list, 0):
        if element in consonants:
            char_list[idx] = value_as_string
    return char_list
