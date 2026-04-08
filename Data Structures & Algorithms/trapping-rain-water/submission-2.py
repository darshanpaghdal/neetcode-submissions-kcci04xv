class Solution:
    def trap(self, height: list[int]) -> int:
        max_left = []
        max_right = [0] * len(height)
        min_of_left_right = []

        current_max_right = 0
        for i in range(len(height)-1,-1,-1):
            max_right[i] = current_max_right

            if height[i] > current_max_right:
                current_max_right = height[i]

        current_max_left = 0
        for i in range(len(height)):
            max_left.append(current_max_left)

            min_of_left_right.append((min(max_left[i], max_right[i])))

            if height[i] > current_max_left:
                current_max_left = height[i]

        total_trapped_water = 0
        for i in range(len(height)):
            trapped_water = min_of_left_right[i] - height[i]
            if trapped_water > 0:
                total_trapped_water += trapped_water

        # print(max_left)
        # print(max_right)
        # print(min_of_left_right)

        return total_trapped_water