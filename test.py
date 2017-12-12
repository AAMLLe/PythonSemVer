import unittest
#from application.app.src.About import is_anagram
#from ..Modules import LDAPManager
#import pakage
#from pakage.About import is_anagram

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
#
#    def test_is_anagram(self):
#        self.assertFalse(is_anagram('acb', 'cdd'))

if __name__ == '__main__':
    unittest.main()
