def soundex(word):
    for letter in 'aeiouyhw':
        word = word.replace(letter, '')
    return word