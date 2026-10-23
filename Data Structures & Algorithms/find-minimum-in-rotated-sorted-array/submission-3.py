class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:    
            s = (l+r) // 2
            if nums[s] > nums[r]:
                l = s + 1
            else:
                r = s
        
            
        return nums[l]

        
        