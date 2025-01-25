import unittest
from LangToken.tokenizer import Tokenizer

class TestTokenizer(unittest.TestCase):
    def setUp(self):
        '''
        Initialize the tokenizer and set some example text for testing
        '''
        self.tokenizer = Tokenizer()
        self.tokenizer.text = "Hello, world! How are you?"
        self.tokenizer.fit()

    def test_fit(self):
        '''
        Check if the tokenizer creates the correct vocab size
        '''
        vocab = self.tokenizer.get_token()
        self.assertGreater(len(vocab), 0, "Vocabulary should not be empty")

    def test_encode_known_tokens(self):
        '''
        Test encoding of a string with known tokens
        '''
        text = "Hello, world!"
        encoded = self.tokenizer.encode(text)
        decoded = self.tokenizer.decode(encoded)
        self.assertEqual(decoded, text, "Decoded text should match the original input")

    def test_encode_unknown_tokens(self):
        '''
        Test encoding of a string with unknown tokens
        '''
        text = "This is unknown!"
        encoded = self.tokenizer.encode(text)
        self.assertIn(self.tokenizer.str_to_int["<|unk|>"], encoded, "Unknown tokens should map to <|unk|>")

    def test_decode(self):
        '''
        Test decoding of encoded IDs
        '''
        encoded = [self.tokenizer.str_to_int[token] for token in ["Hello", ",", "world", "!"]]
        decoded = self.tokenizer.decode(encoded)
        self.assertEqual(decoded, "Hello, world!", "Decoded text should reconstruct the original text")

    def test_pass_file(self):
        '''
        Test reading from a file
        '''
        with open("test_file.txt", "w", encoding="utf-8") as f:
            f.write("Test file content.")
        self.tokenizer.pass_file("test_file.txt", "utf-8")
        self.assertEqual(self.tokenizer.text, "Test file content.", "File content should be loaded correctly")

    def test_get_token(self):
        '''
        Test retrieval of the token-to-integer dictionary
        '''
        tokens = self.tokenizer.get_token()
        self.assertIsInstance(tokens, dict, "get_token should return a dictionary")
        self.assertIn("Hello", tokens, "'Hello' should be in the vocabulary")

    def test_get_token_decoder(self):
        '''
        Test retrieval of the integer-to-token dictionary
        '''
        decoder = self.tokenizer.get_token_decoder()
        self.assertIsInstance(decoder, dict, "get_token_decoder should return a dictionary")
        self.assertIn(0, decoder, "The integer-to-token dictionary should contain valid mappings")

if __name__ == "__main__":
    unittest.main()
