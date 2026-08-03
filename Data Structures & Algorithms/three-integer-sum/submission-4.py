class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        ans = []
        for index in range(len(nums)):

            if nums[index] == nums[index-1] and index > 0:
                continue
            
            i = index+1
            j = len(nums) -1
            diff = -nums[index]


            while i < j:
                twosum = nums[i] + nums[j]

                if twosum == diff:
                    threesum = [nums[i],nums[j],nums[index]]
                    ans.append(threesum)
                    i += 1
                    j -= 1
                    while i < j and nums[i]==nums[i-1]:
                        i += 1
                elif twosum < diff:
                    i += 1

                else:
                    j -= 1
        return ans
                