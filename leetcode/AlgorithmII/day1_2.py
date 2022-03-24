# day 1 problem 33 Search in Rotated sorted array

#slower solution but less memory used
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # handling default answer if target not found
        if target not in nums:
            return -1
        # checking through list to find target
        for i in range(len(nums)):
            if nums[i] == target:
                return i 

#very little more memory used but a lot faster
class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        # checking through list to find target
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        #default case
        return -1

'''improvements maybe split list and check simoltaneously for target''' 