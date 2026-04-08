class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!=len(t):
            return False

        map_list = []
        for sr in [s,t]:
            h_map = {}
            for ch in sr:
                if ch in h_map:
                    h_map[ch] += 1
                else:
                    h_map[ch] = 1

            map_list.append(h_map)

        if map_list[0] == map_list[1]:
            return True
        else:
            return False