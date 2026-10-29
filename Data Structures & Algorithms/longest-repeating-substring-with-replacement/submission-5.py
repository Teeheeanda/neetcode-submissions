from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        if len(s) <= k:
            return len(s)
        
        counts = {}
        maxL = 0
        i = 0
        for j in range(len(s)):
            counts[s[j]] = counts.get(s[j], 0) + 1

            m = (j-i + 1) - max(counts.values())

            while (j - i +1) - max(counts.values()) > k:
                counts[s[i]] -= 1
                i += 1
            maxL = max(maxL, j - i +1)

        return maxL 
        