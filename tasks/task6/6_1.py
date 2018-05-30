import unittest
import fizzbuzz


class FizzBuzzTest(unittest.TestCase):
    def test_business_as_usual(self):
        self.assertEqual(fizzbuzz(1), 1)
        self.assertEqual(fizzbuzz(2), 2)
        self.assertEqual(fizzbuzz(4), 4)

    def test_fizz(self):
        self.assertEqual(fizzbuzz(3), 'fizz')
        self.assertEqual(fizzbuzz(6), 'fizz')
        self.assertEqual(fizzbuzz(99), 'fizz')

    def test_buzz(self):
        self.assertEqual(fizzbuzz(5), 'buzz')
        self.assertEqual(fizzbuzz(10), 'buzz')
        self.assertEqual(fizzbuzz(20), 'buzz')

    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15), 'fizzbuzz')
        self.assertEqual(fizzbuzz(30), 'fizzbuzz')
        self.assertEqual(fizzbuzz(90), 'fizzbuzz')


def main():
    unittest.main()


if __name__ == '__main__':
    main()
