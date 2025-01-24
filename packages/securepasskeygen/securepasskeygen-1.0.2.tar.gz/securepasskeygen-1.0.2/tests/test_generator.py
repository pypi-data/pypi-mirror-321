import unittest
from password_generator.generator import generate_password

class TestPasswordGenerator(unittest.TestCase):
    def test_password_length(self):
        password = generate_password(length=16)
        self.assertEqual(len(password), 16)

    def test_password_complexity(self):
        password = generate_password(length=16, use_uppercase=True, use_numbers=True, use_special_chars=True)
        self.assertTrue(any(c.isupper() for c in password))
        self.assertTrue(any(c.isdigit() for c in password))
        self.assertTrue(any(c in string.punctuation for c in password))

if __name__ == '__main__':
    unittest.main()
