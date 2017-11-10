class Solution(object):
  def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    #checking for lists that are 1 or 0 in length, both of which cannot have a valid transaction
    if len(prices) < 2:
      return 0;
    
    largest_after = -1 #current largst after the current smallest, this value is not needed, but helps in runtiume by being able to compare to it rahter than re-computing the possible profit
    smallest = prices[0]  #current smallest value in array
    profit = 0 #running update on maximum profit
    
    #general idea for the algorithm, since we can't bo back in time, we only care about what comes up after the current smallest is found.
    #as long as we record the current highest profit,we can only care about comparisions starting from the newest smallest subset

    for x in prices:
      #as we go through the find the start of a new smallest subset
      if x < smallest:
        smallest = x
        largest_after = -1 #reset the largest number after the start of the new subset
      elif largest_after < x:
        largest_after = x
        
        #since we got here, we have a new largest_number after the smallest number found so far, we see if it is the current highest profit
        if largest_after - smallest > profit:
          profit = largest_after - smallest
                
    return profit;