print("hello")
ar = [0,10,29,9,7,6,3]
l = 0
r = len(ar)-1
print(ar[r])

def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    answers = []
    for i in range(len(array)-2): # i = current number
        left = i + 1
        right = len(array)-1
        while left < right:
            cs = array[i] + array[left] + array[right]
            if cs == targetSum:
                answers.append([array[i], array[left], array[right]])
                left +=1
                right -=1
            elif cs < targetSum:
                left +=1
            elif cs > targetSum:
                right -= 1
    return answers
threeNumberSum(ay,target)

ay= [0, 59, 30, 10, -2, 49, 17]
target = 57
