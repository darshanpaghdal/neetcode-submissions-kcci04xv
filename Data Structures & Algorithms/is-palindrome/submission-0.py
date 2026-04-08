class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(" ", "")

        for ch in s:
            if not ch.isalpha() and not ch.isdigit():
                print(ch)
                s = s.replace(ch, "")

        print(s)
        if s == s[::-1]:
            return True
        else:
            return False
