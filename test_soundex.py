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
        code = soundex.remove_upper_case_vowels(word)
        self.assertEqual(['L', 'L', 'S'], code)

        word = list('AEIOUHWY')
        code = soundex.remove_upper_case_vowels(word)
        self.assertEqual([], code)

    def test_removes_lover_case_vowels(self):
        word = list('hellooowhys')
        code = soundex.remove_lower_case_vowels(word)
        self.assertEqual(['l', 'l', 's'], code)

        word = list('aeiouwhy')
        code = soundex.remove_lower_case_vowels(word)
        self.assertEqual([], code)

    def test_remove_given_chars(self):
        word_list= list('abpqrsTUVWXxyz')
        code = soundex.remove_given_chars(word_list,'abTUVXx')
        self.assertEqual(['p', 'q', 'r', 's', 'W', 'y', 'z'], code)

if __name__ == '__main__':
    unittest.main( )
