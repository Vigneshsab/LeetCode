class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1=sum1=nums[0]
        for i in range(1, len(nums)):
            if sum1>0:
                sum1+=nums[i]
            else:
                sum1=nums[i]
            max1=max(sum1,max1)
            
        return max1
        