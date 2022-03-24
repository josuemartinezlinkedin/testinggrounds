# Day 2 algorith II problem 153 Find Minimum in Rotated Dorted Array
#easiset solution without creating an algorithm
class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)
'''con, slower and more memory than other solutions'''

class Solution2:
    def findMin(self, nums: List[int]) -> int:
        #checking list up to last value
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return nums[i+1]
        # default first value is min
        return nums[0]