import unittest
import soundex


class SoundexTestCase(unittest.TestCase):
    def test_soundex(self):
        self.assertEqual('T522', soundex.soundex('Tymczak'))
        self.assertEqual('R163', soundex.soundex('Rupert'))
        self.assertEqual('R163', soundex.soundex('Robert'))
        self.assertEqual('P236', soundex.soundex('Pfister'))
        self.assertEqual('H555', soundex.soundex('Honeyman'))
        self.assertEqual('R150', soundex.soundex('Rubin'))
        self.assertEqual('A261', soundex.soundex('Ashcraft'))
        self.assertEqual('A261', soundex.soundex('Ashcroft'))
        self.assertEqual('Q416', soundex.soundex('Qelibari'))
        self.assertEqual('R500', soundex.soundex('Romi'))
        self.assertEqual('B265', soundex.soundex('Bajram'))
        self.assertEqual('R263', soundex.soundex('Rezart'))



class RemoveVowelsTestCase(unittest.TestCase):
    def test_removes_upper_case_vowels(self):
        word = list('HELLOOOOOWHYS')
        code = soundex.remove_upper_and_lower_case_vowels(word)
        self.assertEqual(['L', 'L', 'S'], code)

        word = list('AEIOUHWY')
        code = soundex.remove_upper_and_lower_case_vowels(word)
        self.assertEqual([], code)

    def test_removes_given_chars(self):
        word_list = list('abpqrsTUVWXxyz')
        code = soundex.remove_given_chars(word_list, 'abTUVXx')
        self.assertEqual(['p', 'q', 'r', 's', 'W', 'y', 'z'], code)


class ReplaceCharsTestCase(unittest.TestCase):
    def test_replaces_given_consonants_with_value(self):
        word_list = list('abpqrsTUvWXxyz')
        code = soundex._replace_given_consonants_with_value(word_list, 'bfpv', '1')
        self.assertEqual(list('a11qrsTU1WXxyz'), code)

    def test_removes_duplicates(self):
        char_list = list('111123111212111')
        code = soundex.remove_duplicates(char_list)
        self.assertEqual(list('12312121'), code)

        char_list = list('111222333444555666111')
        code = soundex.remove_duplicates(char_list)
        self.assertEqual(list('1234561'), code)

        char_list = list('1111111111111111')
        code = soundex.remove_duplicates(char_list)
        self.assertEqual(list('1'), code)

        char_list = list('121212')
        code = soundex.remove_duplicates(char_list)
        self.assertEqual(list('121212'), code)

    def test_appends_zeros_if_len_lower_than_4(self):
        char_list = list('R6')
        code = soundex.append_zeros_if_len_lower_than_4(char_list)
        self.assertEqual('R600', code)

if __name__ == '__main__':
    unittest.main( )
