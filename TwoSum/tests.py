def main():
  import sys
  from solution import Solution
  
  print Solution().twoSum([2, 7, 11, 15], 9)
  print 'Expected [0, 1]'

  print Solution().twoSum([11, 15], 26)
  print 'Expected [0, 1]'

  print Solution().twoSum([2, 7, 11, 15], 26)
  print 'Expected [2, 3]'

  print Solution().twoSum([2, 7, 11, 15], 17)
  print 'Expected [0, 3]'

if __name__ == '__main__':
  main()