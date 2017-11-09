import sys, unittest
from solution import Solution

#simple custom class to test equalness of all added expected/given pairs
class TestTwoSum(unittest.TestCase):

  def setUp(self):
    self.pairs = []  
    self.pairs.append( ( 5 , Solution().maxProfit( [7,1,5,3,6,4] ) ) )
    self.pairs.append( ( 0 , Solution().maxProfit( [7,6,4,3,1] ) ) )

  def test_compare(self):
    test = 1
    for x in self.pairs: 
      self.assertEquals( x[0], x[1], 'Test {} failed: {} is not equal to {}'.format(test, x[0], x[1]))
      test+=1

def main(): 
  unittest.main()


if __name__ == '__main__':
  main()