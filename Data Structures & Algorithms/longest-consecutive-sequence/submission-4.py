class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        longest_sequence = 0
        current_sequence = []
        for num in nums:
            if not current_sequence:
                current_sequence.append(num)
                continue
            
            if num == current_sequence[-1]:
                continue
            elif num == current_sequence[-1] + 1:
                current_sequence.append(num)
            else:
                if len(current_sequence) > longest_sequence:
                    longest_sequence = len(current_sequence)
                current_sequence = [num]
        
        if len(current_sequence) > longest_sequence:
            longest_sequence = len(current_sequence)
        
        return longest_sequence



        