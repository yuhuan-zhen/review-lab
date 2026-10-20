import unittest

from app import is_valid_user_id, normalize_user_id


class TestNormalizeUserId(unittest.TestCase):
    def test_lowercases_and_strips(self):
        self.assertEqual(normalize_user_id("  Alice_01 "), "alice_01")

    def test_strips_leading_zeros_for_numeric_ids(self):
        self.assertEqual(normalize_user_id("000123"), "123")

    def test_all_zero_numeric_id_becomes_zero(self):
        self.assertEqual(normalize_user_id("000"), "0")

    def test_keeps_leading_zeros_for_non_numeric_ids(self):
        self.assertEqual(normalize_user_id("007abc"), "007abc")

    def test_empty_raises(self):
        with self.assertRaises(ValueError):
            normalize_user_id("")

    def test_whitespace_only_raises(self):
        with self.assertRaises(ValueError):
            normalize_user_id("   ")

    def test_none_raises(self):
        with self.assertRaises(ValueError):
            normalize_user_id(None)


class TestIsValidUserId(unittest.TestCase):
    def test_accepts_normal_id(self):
        self.assertTrue(is_valid_user_id("alice_01"))

    def test_rejects_too_short(self):
        self.assertFalse(is_valid_user_id("ab"))

    def test_rejects_too_long(self):
        self.assertFalse(is_valid_user_id("a" * 33))

    def test_rejects_illegal_chars(self):
        self.assertFalse(is_valid_user_id("alice 01"))
        self.assertFalse(is_valid_user_id("alice@example"))


if __name__ == "__main__":
    unittest.main()
