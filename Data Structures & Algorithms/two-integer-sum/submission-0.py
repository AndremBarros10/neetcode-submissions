class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        indexList = []

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in prevMap:
                indexList.append(prevMap[diff])
                indexList.append(i)
                return indexList
            prevMap[nums[i]] = i
                
        return indexList