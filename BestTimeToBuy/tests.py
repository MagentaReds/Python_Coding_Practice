import sys, unittest
from solution import Solution

#simple custom class to test equalness of all added expected/given pairs
class TestBestTimeToBuy(unittest.TestCase):

  def setUp(self):
    self.pairs = []  
    self.pairs.append( ( 5 , Solution().maxProfit( [7,1,5,3,6,4] ) ) )
    self.pairs.append( ( 0 , Solution().maxProfit( [7,6,4,3,1] ) ) )

  def test_correct_answers(self):
    test = 1
    for x in self.pairs: 
      self.assertEquals( x[0], x[1], 'Test {} failed: {} is not equal to {}'.format(test, x[0], x[1]))
      test+=1

  def test_empty_input_list(self):
    self.assertEquals(0, Solution().maxProfit( [] ) )
  
  def test_length_one_list(self):
    self.assertEquals(0, Solution().maxProfit( [2] ))

def main(): 
  unittest.main()


if __name__ == '__main__':
  main()