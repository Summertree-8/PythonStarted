class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, num in enumerate(nums):
            if(target - num) in nums:
                if nums.index(target-num) != i:
                    return [i, nums.index(target-num)]