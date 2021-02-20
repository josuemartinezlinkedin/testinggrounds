# Two Number Sum
"""Write a function that takes in a non-empty array of distinct integers and
an integer representing a target sum. If any two numbers in the input array sum
up to the target sum, the function should return them in an array. Assume that
there will be at most one pair of numbers summing up to the target sum"""
array =  [3,5,-4,8, 11, 1, -1, 6]
target = 10
samplesolution = [-1, 11]
'''This solution is in O(nlog(n))| o(1) space '''
def Twonumbersum(array, targetsum):
    array.sort() #we want to make sure lowest to highest
    left = 0 #we want the first position
    right = len(array) - 1 #we want the last position so - 1
    while left < right: #we don't want to go past the length of the array
        currentsum = array[left] + array[right]
        if currentsum == targetsum:
            return [array[left], array[right]]
        elif currentsum < targetsum:
            left += 1
        elif currentsum > targetsum:
            right -= 1
    return []

def Solution3(array, targetsum):
    leftpointer = 0
    rightpointer = len(array)-1
    right = array[-1]
    while leftpointer > rightpointer:
        currentsum = array[leftpointer] + array[rightpointer]
        if currentsum == targetsum:
            return [array[leftpointer], array[rightpointer]]
        elif currentsum < targetsum:
            #if the current sum is less than the target sum then that means
            #that the lowest number is too small and since we sorted the array
            #we have to point to the next one
            leftpointer += 1
        elif currentsum > targetsum:
            #If the current sum is greater than the target sum then that means
            #that the biggest number is too big since it plus the smallest is
            #greater than the targetsum so pointer goes needs to go down one
            rightpointer -= 1
    return [] #if leftpointer is = to or less than the rightpointer we return an
    #empty array since that means that there aren't enough numbers in the array
    #to return 2 positions

def Solution2(array, targetsum):
    #O(n) time | o(n) space
    def Twonumbersum(array, targetsum):
        nums = {}
        for num in array:
            potentialmatch = targetsum - sum
            if potentialmatch in nums:
                return [potentialmatch, num]
            else:
                 nums[num] = True
        return []

def Solution3(array, targetsum):
    for i in range(len(array)-1):
        firstnum = array[i]
        for j in range(i +  1, len(array)):
            sedondnum = array[j]
            if firstnum + secondnum == targetsum:
                return [firstnum, secondnum]
    return []



def mysolution(array, target):
	dicty = {}
	for i in range(len(array)):
		if target - array[i] in dicty:
			return [array[i], dicty[target - array[i]]]
		else:
			dicty[array[i]] = array[i]
	return []


print(array)
print(array.index(3))
array[3] = 4
print(array)
dict = {2:3, 4:5,6:7}
print(dict[2])
dict[8] = 10
print(dict[8])
array[3]
print(dict)
dict[8]

if 3 in dict:print('ok')



for i in range(len(array)):
    if array[i] - target in dict:
        return [dict[target-array[i]], i]
    else:
        dict[array[i]] = i
