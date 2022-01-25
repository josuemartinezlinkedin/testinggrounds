def subarraySort(array):
    # Write your code here.
    min_ooo = float("inf")
    #This means that any number will be less than it
    max_ooo = float("-inf")
    #This means that any number will be greater than it.

    for i in range(len(array)):
        num = array[i]
        if is_out_of_order(i, num, array):
            min_ooo = min(min_ooo, num)
            #Here we are saying we want the min to be whatever number it is
            max_ooo = max(max_ooo, num)
            #Here we are saying we want the max to be whatever number it is

    if min_ooo == float("inf"):
        return[-1,-1]
    left_idx = 0
    while min_ooo >= array[left_idx]:
        left_idx += 1
    right_idx = len(array)-1
    while max_ooo <= array[right_idx]:
        right_idx -=1
    return [left_idx, right_idx]

def is_out_of_order(i, num, array):
    if i == 0:
        return num > array[i + 1]
    #First question is the first number bigger than second?
    #If it is then we want to update our numbers
    if i == len(array) - 1:
    #Second question is if i = the last number in the array then find out if it
    #is less than the number before it
        return num < array[i-1]
    return num > array[i+1] or num < array[i-1]




subarraySort([1,2,4,7,10,11,7,12,6,7,16,18,4])


def practice(array):
    mini = float("inf")
    maxi = float("-inf")
    for i in range(len(array)):
        num = array[i]
        if thisTrue(i, num, array):
            if i == 0:
                return num > array[i+1]
            if






#sample code for inf and -inf
minus = float("-inf")
plus = float("inf")

print(max(plus,100))
print(min(plus,100))

print(max(minus,100))
print(min(minus,100))
