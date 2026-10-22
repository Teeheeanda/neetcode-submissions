import numpy as np
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_map = {}

        max_f = []
        for n in nums: # O(n)
            freq_map[n] =  freq_map.get(n, 0) + 1
        


        while len(max_f) < k:
            mf = max(freq_map.values())
            for k1, v in freq_map.items():
                if v == mf:
                    max_f.append(k1)
                    freq_map[k1] = -1
                    break
                


        return max_f