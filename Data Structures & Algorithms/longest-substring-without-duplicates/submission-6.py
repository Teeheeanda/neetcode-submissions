class Solution:
        def lengthOfLongestSubstring(self, s: str) -> int:
            
            i, n = 0, len(s)

            mini, maxL = i, 0

            if len(s) <= 1:
                return len(s)
            
            maps = {}
            
            while i < n:

                if maps.get(s[i], None) != None:
                    maxL = max(maxL, i - mini)
                    mini = max(mini, maps[s[i]] + 1)
                    maps[s[i]] = i
    
                else:
                    maps[s[i]] = i

                i += 1
            
            maxL = max(maxL, i - mini)
            return maxL
