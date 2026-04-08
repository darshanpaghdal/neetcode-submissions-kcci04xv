class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.upper().replace(" ", "")

        for ch in s:
            if not (ord(ch) >= ord('A') and ord(ch) <= ord('Z')) and not (ord(ch) >= ord('0') and ord(ch) <= ord('9')):
                s = s.replace(ch, "")

        if s == s[::-1]:
            return True
        else:
            return False
