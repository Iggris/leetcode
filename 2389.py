class Solution(object):
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        nums.sort()
        ans=[]
        helper=0
        for i in queries:
            for j in nums:
                if i-j>=0:
                    helper+=1
                    i-=j
                else:
                    break 
            ans.append(helper)
            helper=0
        return ans
/////////////////////////////////////////////////////////////////
class Solution(object):
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        nums.sort()

        prefix = 0
        for idx in range(len(nums)):
            tmp = nums[idx]
            nums[idx] += prefix
            prefix += tmp

        ans = []
        for query in queries:

            left = 0
            right = len(nums)
            while left < right:
                mid = (left + right) // 2

                if nums[mid] > query:
                    right = mid
                else:
                    left = mid + 1

            ans.append(left)

        return ans
