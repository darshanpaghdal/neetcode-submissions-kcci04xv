class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        h_map = {}
        possible_outcomes = []
        for i in range(len(numbers)):
            h_map[numbers[i]] = target - numbers[i]
            if h_map[numbers[i]] in h_map and numbers.index(h_map[numbers[i]]) != i:
                possible_outcomes.append([numbers.index(h_map[numbers[i]]) + 1 , i+1])

        if len(possible_outcomes) == 1:
            return possible_outcomes[0]
        else:
            least_outcome = []
            for outcome in possible_outcomes:
                if not least_outcome:
                    least_outcome = outcome

                if outcome[0] < least_outcome[0]:
                    least_outcome = outcome
            return least_outcome