class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1

        maxH = 0
        while i < j:
            h = (j-i) * min(heights[i], heights[j])

            if h > maxH:
                maxH = h
            
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        
        return maxH