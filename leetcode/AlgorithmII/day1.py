#Day one
#problem 34 Find First and last position of Element in Sorteed Array
class Solution:
    #function annotations 
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #default answer if target not found
        default = [-1,-1] 
        #to check against when target is found
        first = None 
        second = None
        # to stop searching earch time target is found 
        one = 0 
        two = 0

    #default answer
    if target not in nums:
        return default
    #first index value of target when found in list
    while first == None:
        for i in range(len(nums)):
            if nums[i] == target:
                if one == 0:
                    first = i
                    one +=1
     while first == None:
        for i in range(len(reversed)):
            if reversed[i] == target:
                if one == 0:
                    #calculating the index value of second time locating target in reversed list
                    second = -i*((i+1)-len(nums))
                    two +=1
    #returning first and second index value of where target was first and last located
    return [first, second]
    
