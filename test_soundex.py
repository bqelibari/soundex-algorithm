import unittest
import soundex


class SoundexTestCase(unittest.TestCase):
    def test_gets_first_letter(self):
        letter = soundex.get_first_letter('Akloo')
        self.assertEqual('A', letter)
        letter = soundex.get_first_letter('kkloo')
        self.assertEqual('k', letter)


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


class test_replace_consonants(unittest.TestCase):
    def test_replaces_given_consonants_with_value(self):
        word_list = list('abpqrsTUvWXxyz')
        code = soundex.replace_given_consonants_with_value(word_list, 'bfpv', '1')
        self.assertEqual(list('a11qrsTU1WXxyz'), code)


if __name__ == '__main__':
    unittest.main( )
