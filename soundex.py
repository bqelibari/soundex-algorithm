mapping = {'bfpvBFPV': '1', 'cgjkqsxzCGJKQSXZ': '2', 'dtDT': '3', 'lL': '4', 'mnMN': '5', 'rR': '6'}


def soundex(word):
    '''Would it be better to name the variables after the stage of encoding?
    i.e. word_without_whWH etc.'''
    word_to_encode = list(word)
    word_to_encode = remove_given_chars(word_to_encode, 'whWH''')
    word_to_encode = encode_consonants(word_to_encode)
    word_to_encode = remove_duplicates(word_to_encode)
    word_to_encode = remove_upper_and_lower_case_vowels(word_to_encode)
    word_to_encode = get_first_letter(word, word_to_encode)
    word_to_encode = append_zeros_if_len_lower_than_4(word_to_encode)
    return word_to_encode


def get_first_letter(word: str, word_to_encode: list[str]) -> list[str]:
    if word[0] in 'AEIOUWHYaeiouwhy':
        word_to_encode.insert(0, word[0])
    else:
        word_to_encode[0] = word[0]
    return word_to_encode


def remove_upper_and_lower_case_vowels(char_list: list[str]) -> list:
    word_list = char_list
    return remove_given_chars(word_list, 'AEIOUWHYaeiouwhy')


def remove_given_chars(word_list: list[str], chars_to_remove: str) -> list[str]:
    result = [char for char in word_list if char not in chars_to_remove]
    return result


def encode_consonants(word_to_encode: list[str]) -> list[str]:
    '''No test since its only use is to call another function and bc it was
    extracted from soundex() while refactoring'''
    for key, value in mapping.items( ):
        word_to_encode = _replace_given_consonants_with_value(word_to_encode, key, value)
    return word_to_encode


def _replace_given_consonants_with_value(char_list: list[str], consonants: str, value_as_string: str) -> list[str]:
    for idx, element in enumerate(char_list, 0):
        if element in consonants:
            char_list[idx] = value_as_string
    return char_list


def remove_duplicates(char_list: list[str]) -> list[str]:
    old = ''
    for idx, current_char in enumerate(char_list, 0):
        if current_char == old:
            char_list[idx] = ''
        old = current_char
    return remove_given_chars(char_list, '')


def append_zeros_if_len_lower_than_4(code_list: list[str]) -> str:
    while len(code_list) < 6:
        code_list.append('0')
    return ''.join(code_list[0:4])
