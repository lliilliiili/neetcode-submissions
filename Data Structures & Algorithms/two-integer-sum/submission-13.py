class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_hash = {}
        length = len(nums)
        ans = []
        for i in range(length):
            complement = target - nums[i]
            if complement in num_hash:
                ans.append(num_hash[complement])
                ans.append(i)
                return ans
            num_hash[nums[i]] = i