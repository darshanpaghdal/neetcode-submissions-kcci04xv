class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        map = {
            "[": "]",
            "{": "}",
            "(": ")"
        }

        rev_map = {
            "]": "[",
            "}": "{",
            ")": "("
        }

        for ch in s:
            print(stack)
            if ch in map:
                stack.append(ch)
            
            if ch in rev_map:
                if stack and stack[-1] == rev_map[ch]:
                    stack = stack[:-1]
                else:
                    return False

        if stack:
            return False 
        
        return True

         
               