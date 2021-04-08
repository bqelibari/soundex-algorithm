import unittest
from soundex import soundex

class SoundexTestCase(unittest.TestCase):
    def test_retainsFirstLetter(self):
        code = soundex('myword')
        self.assertEqual('m', code[0])

    def test_removesRemainingVowels(self):
        code = soundex('maauoy')
        self.assertEqual('m', code)


if __name__ == '__main__':
    unittest.main( )
