class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        seen=set()
        stack=[start]
        while stack:
            position=stack.pop(0)
            if arr[position]==0:
                return True
            seen.add(position)
            x=position+arr[position]
            y=position-arr[position]
            if x<len(arr) and x not in seen:
                stack.append(x)
            if y>=0 and y not in seen:
                stack.append(y)
        return False
