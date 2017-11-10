import sys, unittest
from solution import Solution

#simple custom class to test equalness of all added expected/given pairs
class TestTwoSum(unittest.TestCase):

  def setUp(self):
    self.pairs = []  
    self.pairs.append( ( [0,1], Solution().twoSum([2, 7, 11, 15], 9) ) )
    self.pairs.append( ( [0,1], Solution().twoSum([11, 15], 26) ) )
    self.pairs.append( ( [2,3], Solution().twoSum([2, 7, 11, 15], 26) ) )
    self.pairs.append( ( [0,3], Solution().twoSum([2, 7, 11, 15], 17) ) )

  def test_correct_answers(self):
    test = 1
    for x in self.pairs: 
      self.assertEquals( x[0], x[1], 'Test {} failed: {} is not equal to {}'.format(test, x[0], x[1]))
      test+=1

def main(): 
  unittest.main()


if __name__ == '__main__':
  main()