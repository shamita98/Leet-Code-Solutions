# Solution 1 
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(list(set(nums)))
        return len(nums)

# Solution 2 (using two pointers)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
    start = 0
        end = len(nums)-1
        while start < end:
           # check LHS
            if nums[start] == nums[start+1]:
                nums.pop(start)
                end -= 1
            else:
                start += 1
            
            # check RHS
            if end == 0:
                break
            elif nums[end] == nums[end-1]:
                nums.pop(end)
            
            end -= 1
        return len(nums)
