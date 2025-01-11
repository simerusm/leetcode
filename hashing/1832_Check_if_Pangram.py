class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # A-Z: 97-122
        ascii_alphabets = set()
        for char in sentence:
            ascii_char_val = ord(char)
            if ascii_char_val >= 97 and ascii_char_val <= 122:
                ascii_alphabets.add(ascii_char_val)
        return len(ascii_alphabets) == 26
