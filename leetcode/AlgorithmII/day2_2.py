#day2 Algorithm II problem 162 Find Peak Element
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #keeping track of peak
        peak = 0
        #going through array and checking neighbors
        for i in range(len(nums)-1):
            if i !=0 or i != len(nums)-1:
                if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                    return i
        #checking list again and pulling out max value
        for i in range(len(nums)):
            if nums[i] == max(nums):
                peak = i
        return peak
'''cons, slower and more memory that other solutions'''


