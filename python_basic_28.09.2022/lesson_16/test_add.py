from unittest import TestCase

from lesson_16 import add


class TestAdd(TestCase):

    def test_positive(self):
        self.assertEqual(4, add(2, 2))

    def test_zeroes(self):
        self.assertEqual(0, add(0, 0))

    def test_strings(self):
        self.assertEqual('heyho', add('hey', 'ho'))

    def test_floats(self):
        self.assertEqual(3.5, add(1.0, 2.5))

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            add(2, 'hello')