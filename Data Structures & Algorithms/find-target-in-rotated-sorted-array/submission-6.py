class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            s = (l+r) // 2

            if nums[s] == target:
                return s
            
            
            if nums[l] <= nums[s]:
                if target == nums[l]:
                    return l
                if target > nums[s] or target < nums[l]:
                    l = s + 1
                else:
                    r = s - 1
            else:
                if target == nums[l]:
                    return l
                if target < nums[s] or target > nums[l]:
                    r = s - 1
                else:
                    l = s
        return -1