import numpy as np
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_map = {}

        max_f = []
        for n in nums: # O(n)
            freq_map[n] =  freq_map.get(n, 0) + 1
        
        freq_map = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)

        return [x[0] for x in freq_map[:k]] 