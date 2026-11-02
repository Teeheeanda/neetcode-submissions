class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums = sorted(nums)

        results = []
        def isValid(i, currentList, total):
            if total == target:
                results.append(currentList.copy())
                return
            
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                currentList.append(nums[j])
                isValid(j, currentList, total + nums[j])
                currentList.pop()
            
        isValid(0, [], 0)
        return results
        
