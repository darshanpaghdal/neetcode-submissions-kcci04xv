class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h_map = {}
        for num in nums:
            if num in h_map:
                h_map[num] += 1
            else:
                h_map[num] = 1
        
        result = []
        for i in range(k):
            m_keys = {k for k,v in h_map.items() if v==max(h_map.values())} 
            result.extend(list(m_keys))

            if len(result) >= k:
                return result[:k]
            
            for key in list(m_keys):
                del h_map[key]
        
        return result

        