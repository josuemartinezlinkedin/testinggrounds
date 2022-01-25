#For a array to be a Monotonic array it either has to be increasing or decreasing
# example 1,2,3,3,3,4 or 1,3,7,8,8,9 but not 1,3,2 or 1,2,2,3,5,4
# Also -1,-2,-2,-100 for decreasing
def isMonotonic(array):
    if [i for i in array] == [i for i in sorted(array, rverse=True)]:
        return True
    elif [i for i in array] == [i for i in sorted(array, rverse)]:
        return True
    else:
        return False
