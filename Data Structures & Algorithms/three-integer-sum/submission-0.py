class Solution:
    def threeSum(self, numbers: list[int]) -> list[int]:
        h_map = {}
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if (numbers[i] + numbers[j]) in h_map:
                    h_map[numbers[i] + numbers[j]].append([numbers[i], numbers[j], i, j])
                else:
                    h_map[numbers[i] + numbers[j]] = [[numbers[i], numbers[j], i, j]]

        # print(h_map)

        output = []
        for i in range(len(numbers)):
            complement = -1 * numbers[i]
            if complement in h_map:
                for r in h_map[complement]:
                    if i not in r[2:]:
                        result = []
                        result.append(numbers[i])
                        result.extend(r[:2])

                        result.sort()
                        if result not in output:
                            output.append(result)
        return output