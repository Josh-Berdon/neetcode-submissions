class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []
        for letter in s:
            if letter.isalnum():
                chars.append(letter.lower())
        i = 0
        j = len(chars) - 1
        while j > i:
            if chars[i] != chars[j]:
                return False
            if chars[i] == chars[j]:
                i += 1
                j -=1
        return True
        