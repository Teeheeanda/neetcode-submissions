class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        map_nums = {}

        for i in range(len(nums)):

            v = map_nums.get(target - nums[i])
            if v != None:
                return [v, i]
            map_nums[nums[i]] = i
    
        
        
        