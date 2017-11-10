import sys, unittest
from solution import Solution

#simple custom class to test equalness of all added expected/given pairs
class TestContainsDuplicates(unittest.TestCase):

  def setUp(self):
    self.pairs = []  
    self.pairs.append( ( False , Solution().containsDuplicate( [7,1,5,3,6,4] ) ) )
    self.pairs.append( ( True , Solution().containsDuplicate( [7,6,4,1,3,1] ) ) )

  def test_correct_answers(self):
    test = 1
    for x in self.pairs: 
      self.assertEquals( x[0], x[1], 'Test {} failed: {} is not equal to {}'.format(test, x[0], x[1]))
      test+=1


def main(): 
  unittest.main()


if __name__ == '__main__':
  main()