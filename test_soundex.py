import unittest
from soundex import soundex


class SoundexTestCase(unittest.TestCase):
    def test_retainsFirstLetter(self):
        code = soundex('myword')
        self.assertEqual('m', code[0])

    def test_removesVovels(self):
        code = soundex('maauoy')
        self.assertEqual('m', code)
        code = soundex('aeiouwhy')
        self.assertEqual('a', code)

    def test_replacesConsonantsWith1(self):
        code = soundex('mbpfvv')
        self.assertEqual('m1',code)

    def test_replacesConsonantsWith2(self):
        code = soundex('cgjkqsxz')
        self.assertEqual('c2',code)

    def test_replacesConsonantsWith3(self):
        code = soundex('mdtdtdt')
        self.assertEqual('m3',code)

    def test_replacesConsonantsWith4(self):
        code = soundex('mllll')
        self.assertEqual('m4',code)

    def test_replacesConsonantsWith5(self):
        code = soundex('mmnmnmn')
        self.assertEqual('m5',code)

    def test_replacesConsonantsWith6(self):
        code = soundex('mrrr')
        self.assertEqual('m6',code)

    def test_fullAlgorithm(self):
        code = soundex("Qelibari")
        self.assertEqual('Q416', code)
        code = soundex("Robert")
        self.assertEqual('R163', code)
        code = soundex("Rupert")
        self.assertEqual('R163', code)

if __name__ == '__main__':
    unittest.main( )
