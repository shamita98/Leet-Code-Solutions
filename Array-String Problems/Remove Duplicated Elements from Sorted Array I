#================
# Solution 1 
#================
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(list(set(nums)))
        return len(nums)

#================
# Solution 2 
#================
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left < right:
           # check LHS
            if nums[left] == nums[left+1]:
                nums.pop(left)
                right -= 1
            else:
                left += 1
            
            # check RHS
            if right == 0:
                break
            elif nums[right] == nums[right-1]:
                nums.pop(right)           
            right -= 1
        return len(nums)

#================
# Solution 3
#================
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i != len(nums)-1:
            if nums[i] == nums[i+1]:
                nums.pop(i+1)
            else:
                i += 1
        
        return len(nums)
