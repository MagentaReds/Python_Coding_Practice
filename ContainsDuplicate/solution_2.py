class Solution(object):
  def containsDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    
    if len(nums) < 2:
      return False
    
    nums.sort()
    
    for x in range( len(nums) - 1 ):
      if nums[x] == nums[x+1]:
        return True

    return False;