class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = []

        for i in range(len(temperatures)):
            stack = []
            result_added = False
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    if not stack:
                        result.append(1)
                    else:
                        result.append(len(stack) + 1)
                    result_added = True
                    break
                else:
                    stack.append(temperatures[j])

            if not result_added:
                result.append(0)

        return result