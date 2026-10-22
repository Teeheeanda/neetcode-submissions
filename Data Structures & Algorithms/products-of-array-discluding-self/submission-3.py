class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        values = [1] * len(nums)

        prev = 1
        for i in range(len(nums)):
            values[i] = prev
            prev *= nums[i]

        prev = 1
        for i in range(len(nums)-1, -1, -1):
            values[i] *= prev
            prev *= nums[i]
        
        return values