import sys, unittest
from solution import Solution

#simple custom class to test equalness of all added expected/given pairs
class TestProductExceptSelf(unittest.TestCase):

  def setUp(self):
    self.pairs = []  
    self.pairs.append( ( [24,12,8,6], Solution().productExceptSelf( [1,2,3,4] ) ) )
    self.pairs.append( ( [60,40,30,24], Solution().productExceptSelf( [2,3,4,5] ) ) )

  def test_correct_answers(self):
    test = 1
    for x in self.pairs: 
      self.assertEquals( x[0], x[1], 'Test {} failed: {} is not equal to {}'.format(test, x[0], x[1]))
      test+=1

  def test_has_one_zero(self):
    self.assertEquals( [0,12,0], Solution().productExceptSelf( [4,0,3] ))

  def test_has_two_zeroes(self):
    self.assertEquals( [0,0,0,0,0,0,0], Solution().productExceptSelf( [1,5,0,3,2,0,4] ))

def main(): 
  unittest.main()


if __name__ == '__main__':
  main()