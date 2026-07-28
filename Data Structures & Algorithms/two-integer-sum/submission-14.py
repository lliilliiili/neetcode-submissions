class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_hash = {}
        length = len(nums)
        for i in range(length):
            complement = target - nums[i]
            if complement in num_hash:

                return [num_hash[complement], i]

            num_hash[nums[i]] = i