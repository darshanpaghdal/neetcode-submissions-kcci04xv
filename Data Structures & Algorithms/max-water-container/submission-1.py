class Solution:
    def maxArea(self, heights: list[int]) -> int:
        def find_water_capacity(h1,h2, distance):

            if distance < 0:
                distance *= -1

            min_height = min(h1, h2)

            return min_height * distance

        max_capicity = 0

        left = 0
        right = len(heights) - 1

        while left < right:

            cap = find_water_capacity(heights[left], heights[right], right-left)
            if cap > max_capicity:
                max_capicity = cap

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return max_capicity