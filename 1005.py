class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        i=0
        while i<len(nums):
            if k==0:
                return sum(nums)
            else:
                nums[i]=nums[i]*(-1)
                k-=1
                if i<len(nums)-1:
                    if nums[i+1]<=0:
                        i+=1
                    else:
                        if abs(nums[i])>nums[i+1]:
                            i+=1
                
        return sum(nums)
