class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []

        for index in range(len(nums)):
            if nums[index] > 0:
                break

            if index > 0 and nums[index] == nums[index-1]:
                continue

            i = index + 1
            j = len(nums)-1
            diff = nums[index]*(-1)

            

            while i<j:
    
                if  nums[i] + nums[j] ==diff:
                    
                    zerosum = [nums[i],nums[j],nums[index]]
                    ans.append(zerosum)
                    i +=1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1

                elif nums[i] + nums[j] < diff:
                    i+=1
                else :
                    j-=1

        return ans