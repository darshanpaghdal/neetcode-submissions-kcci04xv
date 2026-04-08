class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        signs = ["+", "-", "/", "*"]

        
        for ele in tokens:
            print(stack)
            if ele not in signs:
                stack.append(int(ele))
            
            else:
                if ele == "+":
                    res = stack[-1] + stack[-2]
                elif ele == "-":
                    res = stack[-2] - stack[-1]  
                elif ele == "*":
                    res = stack[-1] * stack[-2]
                elif ele == "/":
                    res = int(stack[-2] / stack[-1])
            
                stack = stack[:-2]
                stack.append(res)

        return stack[0]


    
