class Solution:
    def maxArea(self, heights: list[int]) -> int:
        def find_water_capacity(h1,h2, distance):

            if distance < 0:
                distance *= -1

            min_height = min(h1, h2)

            return min_height * distance

        max_capicity = 0
        for i in range(len(heights)-1):
            for j in range(1, len(heights)):
                cap = find_water_capacity(heights[i], heights[j], j-i)
                if cap > max_capicity:
                    max_capicity = cap

        return max_capicity