import unittest

from ziploc.main import decrypt, encrypt


class TestDatabag(unittest.TestCase):
    def setUp(self):
        """Set up the password and sample data for testing."""
        self.password = (
            "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"
        )
        self.sample_string = "test"
        self.sample_dict = {
            "key1": "value1",
            "nested": {"key2": "value2", "key3": {"key4": "value4"}},
        }
        self.empty_dict = {}

    def test_encrypt_decrypt_string(self):
        """Test encryption and decryption of a simple string."""
        encrypted = encrypt(self.sample_string, self.password)
        decrypted = decrypt(encrypted, self.password)
        self.assertEqual(decrypted, self.sample_string)

    def test_encrypt_decrypt_nested_dict(self):
        """Test encryption and decryption of a nested dictionary."""
        encrypted = encrypt(self.sample_dict, self.password)
        decrypted = decrypt(encrypted, self.password)
        self.assertEqual(decrypted, self.sample_dict)

    def test_encrypt_decrypt_empty_dict(self):
        """Test encryption and decryption of an empty dictionary."""
        encrypted = encrypt(self.empty_dict, self.password)
        decrypted = decrypt(encrypted, self.password)
        self.assertEqual(decrypted, self.empty_dict)

    def test_decrypt_invalid_string(self):
        """Test decryption with invalid encrypted string format."""
        invalid_encrypted = "invalid_data"
        with self.assertRaises(ValueError):
            decrypt(invalid_encrypted, self.password)

    def test_decrypt_wrong_password(self):
        """Test decryption with the wrong password."""
        encrypted = encrypt(self.sample_string, self.password)
        wrong_password = "abcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdef"
        with self.assertRaises(ValueError):
            decrypt(encrypted, wrong_password)

    def test_encrypt_decrypt_edge_cases(self):
        """Test edge cases like empty string and deeply nested structures."""
        # Empty string
        encrypted_empty = encrypt("", self.password)
        decrypted_empty = decrypt(encrypted_empty, self.password)
        self.assertEqual(decrypted_empty, "")

        # Deeply nested structure
        deeply_nested = {"level1": {"level2": {"level3": {"level4": "deep_value"}}}}
        encrypted_deep = encrypt(deeply_nested, self.password)
        decrypted_deep = decrypt(encrypted_deep, self.password)
        self.assertEqual(decrypted_deep, deeply_nested)


if __name__ == "__main__":
    unittest.main()
