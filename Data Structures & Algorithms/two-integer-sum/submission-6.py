class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for i, n in enumerate(nums):
            # Add n to indices with i index
            indices[n] = i

        for i, n in enumerate(nums):
            # Calc target - n to get the diff value
            diff = target - n
            
            # Search for diff in the hash
                # flag for different indices
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
        return []