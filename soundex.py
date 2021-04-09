def soundex(word):
    result = []
    mapping = {'aeiouywh': '', 'bfpv': '1', 'cgjkqsxz': '2', 'dt': '3', 'l': '4', 'mn': '5', 'r': '6'}
    for index, letter in enumerate(word, 1):
        for key in mapping.keys( ):
            if letter in key:
                result.append(mapping[key])
    result[0] = word[:1]
    if len(result) < 3:
        result.append('0')
    result = list(dict.fromkeys(result))
    return ''.join(result)
