class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums = sorted(nums)
        n = len(nums)
        for i in range(0, n - 2):
            j = i + 1
            k = n - 1
            while j != k:
                s2 = nums[j] + nums[k]
                if s2 == -nums[i]:
                    if [nums[i], nums[j], nums[k]] not in res:
                        res += [[nums[i], nums[j], nums[k]]]
                        continue    
                    
                if s2 < -nums[i]:
                    j += 1
                else:
                    k -= 1
        
        return res