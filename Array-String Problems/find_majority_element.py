# ==========================================================
# Solution 1
# Inspired by Moore's Voting Algorithm
# Time complexity = O(n)
# Space complexity = O(1)
# ==========================================================
class Solution:
def majorityElement(self, nums: List[int]) -> int:
  count = 0
  element = 0  
  for n in nums:
      if count == 0:
          element = n
          count = 1
      elif element == n:
          count += 1
      else:
          count -= 1  
  return element
       
# ==========================================================
# Solution 2
# Time complexity = O(nlogn)
# Space complexity = O(1)
# ==========================================================
import math
class Solution:
  def majorityElement(self, nums: List[int]) -> int:
    nums = sorted(nums)
    majority_index = math.trunc(len(nums)/2)
    return nums[majority_index]
    
# ==========================================================
# Solution 3
# Time complexity = O(n^2)
# Space complexity = O(1)
# ==========================================================
class Solution:
  def majorityElement(self, nums: List[int]) -> int:
      unique_elements = list(set(nums))
      for i in range(len(unique_elements)):
          count = nums.count(unique_elements[i])
          if count > len(nums)/2:
              majority = unique_elements[i]
              unique_elements.clear()
              return majority
          
