class Solution:
    def threeSum(self, numbers: list[int]) -> list[int]:
        numbers.sort()

        output = []
        for i in range(1, len(numbers)-1):
            left = 0
            right = len(numbers) - 1

            while left < right and left < i and right > i:

                if numbers[left] + numbers[right] + numbers[i] > 0:
                    right -= 1
                elif numbers[left] + numbers[right] + numbers[i] < 0:
                    left += 1
                elif numbers[left] + numbers[right] + numbers[i] == 0:
                    if [numbers[left], numbers[i], numbers[right]] not in output:
                        output.append([numbers[left], numbers[i], numbers[right]])
                    left += 1
                    right -= 1


        return output