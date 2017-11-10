#O(n) complexity, O(n) space solution
class Solution(object):
  def productExceptSelf(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    N = len(nums)

    myList = [1 for x in range(N)]  #stores the running product from left to right
    myListRight = [1 for x in range(N)] #stores the running product from right to left

    output = [1 for x in range(N)] #stores the output


    #initial value setting for the lists
    myList[0] = nums[0]
    myListRight[N-1] = nums[N-1]

    #N complexity, computes both running products at the same time, left to right, and right to left
    for x in range(1, N):
      myList[x] = nums[x] * myList[x-1]
      myListRight[N-1-x] = nums[N-1-x] * myListRight[N-1-x+1]
    
    #N Complexity, to get the output, we just need to combine the running product from the left to right, and the right to left
    #at index X, we do this by myList[X-1]*myListRight[X+1], 
    #myList[X-1] is the running total of all the numbers before X in nums
    #myListRight[X+1] is the running total of all the numbers after X in nums
    #combine the two and you get the product of all the numbers in nums besides the Xth number
    for x in range(N):
      if x == 0:
        output[x] = myListRight[1]
      elif x == N-1:
        output[x] = myList[x-1]
      else:
        output[x] = myList[x-1] * myListRight[x+1]

    #O(n) complexity, O(n) space
    return output