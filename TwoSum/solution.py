class Solution(object):
  def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    length = len(nums)
    for num1 in range(0, length-1):
      for num2 in range(num1+1, length):
        print 
        if (nums[num1] + nums[num2] == target):
          return [num1, num2]