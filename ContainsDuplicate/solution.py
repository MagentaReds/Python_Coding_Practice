class Solution(object):
  def containsDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    
    if len(nums) < 2:
      return false
    
    myList = []
    
    for x in nums:
      if x in myList:
        return true
      else:
        myList.append(x)

    return False;