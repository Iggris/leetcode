class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)
        left=0
        right=n-1
        maxarea=float("-inf")
        while left<=right:
            maxarea=max(maxarea,(right-left)*min(height[left],height[right]))
            if height[left]>height[right]:
                right-=1
            else:
                left+=1
        return maxarea

        
