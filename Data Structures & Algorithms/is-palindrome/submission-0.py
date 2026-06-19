class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char.lower() for char in s if char.isalnum())
        if s == "".join(reversed(s)):
            return True
        else:
            return False
