class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            comp=target-nums[i]
            if comp in nums and nums.index(comp)!=i:
                return ([i, nums.index(comp)])