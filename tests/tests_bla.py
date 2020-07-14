import unittest

def display_name(name):
    return name.capitalize()

class TestBla(unittest.TestCase):

    def test_name_1(self):
        self.assertEqual(display_name('shady'), 'Shady')

    def test_name_2(self):
        self.assertEqual(display_name('Shady'), 'Shady')

if __name__ == '__main__':
    unittest.main()
